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
        result['question_id'] = result['question_id'].astype(str)
        result['bill_id'] = result['bill_id'].astype(str)
        result['asked_user_id'] = result['asked_user_id'].astype(str)
        return result

    def get_questions_for_user(self, user_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.questions_asked where asked_user_id = :user_id")
        query = query.bindparams(user_id=user_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def save_question(self, bill_id, asked_user_id, question, answer):
        conn = get_connection()
        query = sa.text(f"insert into bill_gpt.questions_asked (bill_id, asked_user_id, question, answer) "
                        f"values(:bill_id, :asked_user_id, :question, :answer)")
        query = query.bindparams(bill_id=bill_id, asked_user_id=asked_user_id, question=question, answer=answer)
        conn.execute(query)
        conn.commit()
        conn.close()
        return True