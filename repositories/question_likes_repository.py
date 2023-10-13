from repositories.db_utils import get_connection
import pandas as pd
import sqlalchemy as sa

class QuestionLikesRepository:
    def get_likes_for_question(self, question_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.question_likes where question_id = :question_id")
        query = query.bindparams(question_id=question_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_likes_for_user(self, user_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.question_likes where user_id = :user_id")
        query = query.bindparams(user_id=user_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_like_ct_for_question(self, question_id):
        conn = get_connection()
        query = sa.text(f"SELECT count(*) FROM bill_gpt.question_likes where question_id = :question_id")
        exe = conn.execute(query)
        row_count = exe.scalar()
        conn.commit()
        conn.close()
        return row_count

    def get_like_counts_for_questions_in_bill(self, bill_id):
        conn = get_connection()
        query = sa.text(f"SELECT question_id, count(*) FROM bill_gpt.question_likes where bill_id = :bill_id group by question_id")
        query = query.bindparams(bill_id=bill_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result
