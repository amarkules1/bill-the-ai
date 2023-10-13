import datetime
import uuid

import pandas as pd

from repositories.db_utils import get_connection
import sqlalchemy as sa
import pytz

class UserAccountRepository:

    def create_user(self, user_name, email, password, feature_emails):
        conn = get_connection()
        query = sa.text("insert into bill_gpt.user_account (user_name, email, password, feature_emails) "
                        "values(:user_name, :email, :password, :feature_emails)")
        query = query.bindparams(user_name=user_name, email=email, password=password, feature_emails=feature_emails)
        conn.execute(query)
        conn.commit()
        conn.close()

    def login(self, email_user, password):
        conn = get_connection()
        query = sa.text("select user_name, email, feature_emails, email_verified, session_token, session_token_expires_at "
                        " from bill_gpt.user_account where (email = :email_user or user_name = :email_user)"
                        " and password = :password and email_verified = true")
        query = query.bindparams(email_user=email_user, password=password)
        result = pd.read_sql(query, conn)
        if len(result) == 0:
            return None
        if result['session_token_expires_at'][0] is None or result['session_token_expires_at'][0] < pytz.UTC.localize(datetime.datetime.now()):
            session_token = str(uuid.uuid4())
            session_token_expires_at = datetime.datetime.now() + datetime.timedelta(days=1)
            query = sa.text("update bill_gpt.user_account set session_token = :session_token, session_token_expires_at = :session_token_expires_at "
                            "where user_id = :user_id")
            query = query.bindparams(session_token=session_token, session_token_expires_at=session_token_expires_at,
                                     user_id=result['user_id'][0])
            conn.execute(query)
            conn.commit()
            result['session_token'] = session_token
            result['session_token_expires_at'] = session_token_expires_at
        result['session_token'] = result['session_token'].astype(str)

        conn.commit()
        conn.close()
        return result

    def verify_email(self, email, email_verification_token):
        conn = get_connection()
        query = sa.text("select count(*) from bill_gpt.user_account where email = :email "
                        "and email_verification_token = :email_verification_token")
        query = query.bindparams(email=email, email_verification_token=email_verification_token)
        result = conn.execute(query)
        row_count = result.scalar()
        success = row_count > 0
        if success:
            query = sa.text("update bill_gpt.user_account set email_verified = true where email = :email")
            query = query.bindparams(email=email)
            conn.execute(query)
        conn.commit()
        conn.close()
        return success

    def login_by_token(self, session_token):
        conn = get_connection()
        query = sa.text("select user_name, email, feature_emails, email_verified, session_token, session_token_expires_at "
                        "from bill_gpt.user_account where session_token = :session_token and session_token_expires_at > now() and email_verified = true")
        query = query.bindparams(session_token=session_token)
        result = pd.read_sql(query, conn)
        if len(result) == 0:
            return None
        result['session_token'] = result['session_token'].astype(str)
        conn.commit()
        conn.close()
        return result

    def get_user_by_id(self, user_id):
        conn = get_connection()
        query = sa.text("select user_name, user_id, email, feature_emails, email_verified, session_token, session_token_expires_at "
                        "from bill_gpt.user_account where user_id = :user_id")
        query = query.bindparams(user_id=user_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_user_by_email(self, email):
        conn = get_connection()
        query = sa.text("select user_name, user_id, email, feature_emails, email_verified, session_token, session_token_expires_at "
                        "from bill_gpt.user_account where email = :email")
        query = query.bindparams(email=email)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_user_by_user_name(self, user_name):
        conn = get_connection()
        query = sa.text("select user_name, user_id, email, feature_emails, email_verified, session_token, session_token_expires_at "
                        "from bill_gpt.user_account where user_name = :user_name")
        query = query.bindparams(user_name=user_name)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_verification_token(self, email):
        conn = get_connection()
        query = sa.text("select email_verification_token from bill_gpt.user_account where email = :email")
        query = query.bindparams(email=email)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result['email_verification_token'][0] if len(result) > 0 else None
