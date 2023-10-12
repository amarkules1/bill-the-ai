from repositories.db_utils import get_connection
import pandas as pd
import sqlalchemy as sa

class QuestionsAskedRepository:

    def get_questions_for_bill(self, bill_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.questions_asked where bill_id = :bill_id")
        query = query.bindparams(bill_id=bill_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_questions_for_user(self, user_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.questions_asked where asked_user_id = :user_id")
        query = query.bindparams(user_id=user_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result