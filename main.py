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

from email_verification import welcome_email

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

dppa_vector_store = PGVectorStore.from_params(
    database="postgres",
    host=url.host,
    password=url.password,
    port=url.port,
    user=url.username,
    table_name="data_privacy_and_protection_act",
    embed_dim=1536,  # openai embedding dimension
)
dppa_index = VectorStoreIndex.from_vector_store(vector_store=dppa_vector_store)
index_lookup = {
    "ira": ira_index,
    "fra": fra_index,
    "dppa": dppa_index
}

openai.api_key = os.getenv("OPENAI_API_KEY")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$')


@app.route('/')
def hello():
    return redirect("/index.html", code=302)


@app.route('/ira-q-and-a')
def ira_q_and_a():
    df = get_bill_questions_and_answers("ira")
    return df.to_json(orient="records")


@app.route('/fra-q-and-a')
def fra_q_and_a():
    df = get_bill_questions_and_answers("fra")
    return df.to_json(orient="records")


@app.route('/dppa-q-and-a')
def fra_q_and_a():
    df = get_bill_questions_and_answers("dppa")
    return df.to_json(orient="records")


@app.route('/ira-query')
def ira_query():
    query = request.args.get('query')
    if query is None or len(query) < 20:
        return {}
    df = get_bill_questions_and_answers("ira")
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
    df = get_bill_questions_and_answers("fra")
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


@app.route('/dppa-query')
def fra_query():
    query = request.args.get('query')
    if query is None or len(query) < 20:
        return {}
    df = get_bill_questions_and_answers("dppa")
    most_similar_score = 0
    answer_row = None
    for i, row in df.iterrows():
        score = get_similarity_score(query, row['question'])
        if score > most_similar_score and score > 0.85:
            most_similar_score = score
            answer_row = row
    if answer_row is None:
        answer_row = run_query(query, "dppa")
    return answer_row.to_json()


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


def run_query(query, bill_id):
    answer = str(index_lookup[bill_id].as_query_engine().query(query))
    conn = get_connection()
    ins = sqlalchemy.text(f"INSERT INTO bill_gpt.{bill_id}_questions_and_answers (question, answer) "
                          f"VALUES (:query, :answer)")
    ins = ins.bindparams(query=query, answer=answer)
    conn.execute(ins)
    conn.commit()
    conn.close()
    return pd.Series(data={"answer": answer, "question": query})


def get_bill_questions_and_answers(bill_id):
    conn = get_connection()
    df = pd.read_sql(sql.text(f"SELECT * FROM bill_gpt.{bill_id}_questions_and_answers"), conn)
    conn.commit()
    conn.close()
    return df


def get_connection():
    return sqlalchemy.create_engine(os.getenv("LINODE_CONN_STRING")).connect()


def get_similarity_score(st1, st2):
    return 1 - (lev(st1, st2) / max(len(st1), len(st2)))
