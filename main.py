import re
import uuid

from flask import Flask, request, redirect
import pandas as pd
import sqlalchemy
from sqlalchemy import sql
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import logging
import os
from Levenshtein import distance as lev
from sqlalchemy import make_url
import openai
from llama_index.vector_stores import PGVectorStore
from llama_index.indices.vector_store import VectorStoreIndex

from dotenv import load_dotenv, find_dotenv

from email_verification import welcome_email, account_verification, password_reset
from repositories.bill_details_repository import BillDetailRepository
from repositories.questions_asked_repository import QuestionsAskedRepository
from repositories.user_account_repository import UserAccountRepository

_ = load_dotenv(find_dotenv())  # read local .env file

# create console logger and file logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler1)
handler2 = logging.FileHandler('bill-the-ai-log.txt')
handler2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler2)


# Flask setup
app = Flask(__name__, static_folder='bill-ai-frontend/dist', static_url_path='')
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["300 per hour", "30 per minute"],
    storage_uri="memory://",
)
CORS(app)

connection_string = os.getenv("LINODE_CONN_STRING")
url = make_url(connection_string)
ira_vector_store = PGVectorStore.from_params(
    database="postgres",
    host=url.host,
    password=url.password,
    port=url.port,
    user=url.username,
    table_name="inflation_reduction_act",
    embed_dim=1536,  # openai embedding dimension
)
ira_index = VectorStoreIndex.from_vector_store(vector_store=ira_vector_store)

fra_vector_store = PGVectorStore.from_params(
    database="postgres",
    host=url.host,
    password=url.password,
    port=url.port,
    user=url.username,
    table_name="fiscal_responsibility_act",
    embed_dim=1536,  # openai embedding dimension
)
fra_index = VectorStoreIndex.from_vector_store(vector_store=fra_vector_store)

chips_vector_store = PGVectorStore.from_params(
    database="postgres",
    host=url.host,
    password=url.password,
    port=url.port,
    user=url.username,
    table_name="chips_act",
    embed_dim=1536,  # openai embedding dimension
)
chips_index = VectorStoreIndex.from_vector_store(vector_store=chips_vector_store)
index_lookup = {
    "ira": ira_index,
    "fra": fra_index,
    "chips": chips_index
}

openai.api_key = os.getenv("OPENAI_API_KEY")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$')

user_account_repository = UserAccountRepository()
bill_details_repository = BillDetailRepository()
questions_asked_repository = QuestionsAskedRepository()


@app.route('/')
def hello():
    return redirect("/index.html", code=302)


@app.route('/ira-q-and-a')
def ira_q_and_a():
    df = get_bill_questions_and_answers_by_alias("ira")
    return df.to_json(orient="records")


@app.route('/fra-q-and-a')
def fra_q_and_a():
    df = get_bill_questions_and_answers_by_alias("fra")
    return df.to_json(orient="records")


@app.route('/chips-q-and-a')
def chips_q_and_a():
    df = get_bill_questions_and_answers_by_alias("chips")
    return df.to_json(orient="records")


@app.route('/ira-query')
def ira_query():
    query = request.args.get('query')
    if query is None or len(query) < 20:
        return {}
    df = get_bill_questions_and_answers_by_alias("ira")
    most_similar_score = 0
    answer_row = None
    for i, row in df.iterrows():
        score = get_similarity_score(query, row['question'])
        if score > most_similar_score and score > 0.85:
            most_similar_score = score
            answer_row = row
    if answer_row is None:
        answer_row = run_query(query, "ira")
    return answer_row.to_json()


@app.route('/fra-query')
def fra_query():
    query = request.args.get('query')
    if query is None or len(query) < 20:
        return {}
    df = get_bill_questions_and_answers_by_alias("fra")
    most_similar_score = 0
    answer_row = None
    for i, row in df.iterrows():
        score = get_similarity_score(query, row['question'])
        if score > most_similar_score and score > 0.85:
            most_similar_score = score
            answer_row = row
    if answer_row is None:
        answer_row = run_query(query, "fra")
    return answer_row.to_json()


@app.route('/chips-query')
def chips_query():
    query = request.args.get('query')
    if query is None or len(query) < 20:
        return {}
    df = get_bill_questions_and_answers_by_alias("chips")
    most_similar_score = 0
    answer_row = None
    for i, row in df.iterrows():
        score = get_similarity_score(query, row['question'])
        if score > most_similar_score and score > 0.85:
            most_similar_score = score
            answer_row = row
    if answer_row is None:
        answer_row = run_query(query, "chips")
    return answer_row.to_json()


@app.route('/bill-summary')
def bill_summary():
    bill_id = request.args.get('bill_id')
    df = bill_details_repository.get_by_bill_alias(bill_id)
    if df.shape[0] == 0:
        return {}
    return df.iloc[0].to_json()


@app.route('/subscribe', methods=['POST'])
def subscribe():
    body = request.get_json()
    if body is None or body['email'] is None or not EMAIL_REGEX.match(body['email']):
        return {"error": "Please provide a valid email address"}, 400
    conn = get_connection()
    exists = sqlalchemy.text(f"SELECT * FROM bill_gpt.bill_update_subscribers WHERE email = :email")
    exists = exists.bindparams(email=body['email'])
    result = pd.read_sql(exists, conn)
    verification_id = uuid.uuid4()
    if result.shape[0] == 0:
        ins = sqlalchemy.text("INSERT INTO bill_gpt.bill_update_subscribers (name, email, verification_id, is_active) "
                              "VALUES (:name, :email, :id, FALSE)")
        ins = ins.bindparams(name=body['name'] if 'name' in body.keys() else None,
                             email=body['email'], id=verification_id)
        conn.execute(ins)
    else:
        verification_id = result['verification_id'][0]
    welcome_email.send_email(body['email'], verification_id)
    conn.commit()
    conn.close()
    return {"success": True}


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    body = request.get_json()
    if body is None or body['email'] is None or not EMAIL_REGEX.match(body['email']):
        return {"error": "Please provide a valid email address"}, 400
    conn = get_connection()
    ins = sqlalchemy.text("UPDATE bill_gpt.bill_update_subscribers SET unsubscribe_dt = NOW(), is_active = FALSE"
                          " WHERE email = :email")
    ins = ins.bindparams(email=body['email'])
    conn.execute(ins)
    conn.commit()
    conn.close()
    return {"success": True}


@app.route('/feedback', methods=['POST'])
def feedback():
    body = request.get_json()
    conn = get_connection()
    ins = sqlalchemy.text("INSERT INTO bill_gpt.app_feedback (feedback, email) "
                          "VALUES (:feedback, :email)")
    ins = ins.bindparams(email=body['email'] if 'email' in body.keys() else None,
                         feedback=body['feedback'])
    conn.execute(ins)
    conn.commit()
    conn.close()
    return {"success": True}


@app.route('/verify-email', methods=['POST'])
def verify_email():
    body = request.get_json()
    if body is None or 'email' not in body.keys() or 'id' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    conn = get_connection()
    query = sqlalchemy.text(
        f"SELECT * FROM bill_gpt.bill_update_subscribers WHERE email = :email and verification_id = :id")
    query = query.bindparams(email=body['email'], id=body['id'])
    result = conn.execute(query)
    if result.rowcount == 0:
        return {"error": "Invalid Verification Code"}, 400
    upd = sqlalchemy.text(f"UPDATE bill_gpt.bill_update_subscribers SET is_active = true WHERE email = :email")
    upd = upd.bindparams(email=body['email'])
    conn.execute(upd)
    conn.commit()
    conn.close()
    return {"success": True}


@app.route('/verify-account', methods=['POST'])
def verify_account():
    body = request.get_json()
    if body is None or 'email' not in body.keys() or 'token' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    user_account_repository.verify_email(body['email'], body['token'])
    return {"success": True}


@app.route('/create-account', methods=['POST'])
def create_account():
    body = request.get_json()
    #required fields: email, password, user_name
    if body is None or 'email' not in body.keys() or 'password' not in body.keys() or 'user_name' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    email = body['email']
    password = body['password']
    user_name = body['user_name']
    feature_emails = body['feature_emails'] if 'feature_emails' in body.keys() else False
    if not EMAIL_REGEX.match(email):
        return {"error": "Please provide a valid email address"}, 400
    if len(user_account_repository.get_user_by_email(email)) > 0:
        return {"error": "Email already in use"}, 400
    if len(user_account_repository.get_user_by_user_name(user_name)) > 0:
        return {"error": "Username already in use"}, 400
    user_account_repository.create_user(user_name, email, password, feature_emails)
    verification_token = user_account_repository.get_verification_token(email)
    account_verification.send_email(email, verification_token)
    return {"success": True}

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    if body is None:
        return {"error": "Missing Request Params"}, 400
    if 'token' in body.keys():
        token = body['token']
        result = user_account_repository.login_by_token(token)
        if result is None:
            return {"error": "Invalid Token"}, 400
        return result.iloc[0].to_json()
    if 'email_user' not in body.keys() or 'password' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    email_user = body['email_user']
    password = body['password']
    result = user_account_repository.login(email_user, password)
    if result is None:
        return {"error": "Invalid Credentials"}, 400
    return result.iloc[0].to_json()


@app.route('/send-password-reset', methods=['POST'])
def send_password_reset():
    body = request.get_json()
    if body is None or 'email' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    email = body['email']
    token = user_account_repository.generate_reset_token(email)
    if token is not None:
        password_reset.send_email(email, token)
        return {"success": True}
    return {"error": "Invalid Email"}, 400


@app.route('/validate-password-reset', methods=['POST'])
def validate_password_reset():
    body = request.get_json()
    if body is None or 'email' not in body.keys() or 'token' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    email = body['email']
    token = body['token']
    if not EMAIL_REGEX.match(email):
        return {"error": "Please provide a valid email address"}, 400
    if user_account_repository.validate_reset_token(email, token):
        return {"success": True}
    return {"error": "Invalid Token"}, 400


@app.route('/reset-password', methods=['POST'])
def reset_password():
    body = request.get_json()
    if body is None or 'email' not in body.keys() or 'token' not in body.keys() or 'password' not in body.keys():
        return {"error": "Missing Request Params"}, 400
    email = body['email']
    token = body['token']
    password = body['password']
    if not EMAIL_REGEX.match(email):
        return {"error": "Please provide a valid email address"}, 400
    if user_account_repository.validate_reset_token(email, token):
        user_account_repository.reset_password(email, token, password)
        return {"success": True}
    return {"error": "Invalid Token"}, 400


def run_query(query, bill_alias, user_id=None):
    answer = str(index_lookup[bill_alias].as_query_engine().query(query))
    bill_id = bill_details_repository.get_by_bill_alias(bill_alias)['bill_id'][0]
    questions_asked_repository.save_question(bill_id, user_id, query, answer)
    return pd.Series(data={"answer": answer, "question": query})


def get_bill_questions_and_answers_by_alias(alias):
    conn = get_connection()
    bill_details = bill_details_repository.get_by_bill_alias(alias)
    bill_id = str(bill_details['bill_id'][0])
    df = questions_asked_repository.get_questions_for_bill(bill_id)
    conn.commit()
    conn.close()
    return df


def get_connection():
    return sqlalchemy.create_engine(os.getenv("LINODE_CONN_STRING")).connect()


def get_similarity_score(st1, st2):
    return 1 - (lev(st1, st2) / max(len(st1), len(st2)))

if __name__ == '__main__':
    app.run()