from repositories.db_utils import get_connection
import pandas as pd
import sqlalchemy as sa


class BillLikesRepository:
    def get_like_ct_for_bill(self, bill_id):
        conn = get_connection()
        query = sa.text(f"SELECT count(*) FROM bill_gpt.bill_likes where bill_id = :bill_id")
        exe = conn.execute(query)
        row_count = exe.scalar()
        conn.commit()
        conn.close()
        return row_count

    def get_all_like_counts(self):
        conn = get_connection()
        query = sa.text(f"SELECT bill_id, count(*) FROM bill_gpt.bill_likes group by bill_id")
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_likes_for_user(self, user_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM bill_gpt.bill_likes where user_id = :user_id")
        query = query.bindparams(user_id=user_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result
    