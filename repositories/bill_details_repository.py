from repositories.db_utils import get_connection
import pandas as pd
import sqlalchemy as sa


class BillDetailRepository:
    table_name = 'bill_gpt.bill_details_v2'

    def get_all(self):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM {self.table_name}")
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_by_bill_id(self, bill_id):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM {self.table_name} where bill_id = :bill_id")
        query = query.bindparams(bill_id=bill_id)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def get_by_bill_alias(self, bill_alias):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM {self.table_name} where bill_alias = :bill_alias")
        query = query.bindparams(bill_alias=bill_alias)
        result = pd.read_sql(query, conn)
        result['bill_id'] = result['bill_id'].astype(str)
        conn.commit()
        conn.close()
        return result

    def get_by_bill_title(self, bill_title):
        conn = get_connection()
        query = sa.text(f"SELECT * FROM {self.table_name} where bill_title = :bill_title")
        query = query.bindparams(bill_title=bill_title)
        result = pd.read_sql(query, conn)
        conn.commit()
        conn.close()
        return result

    def create(self, bill_id, summary, bill_title, bill_alias, wiki_link, full_text_link):
        conn = get_connection()
        query = sa.text(f"insert into {self.table_name} (bill_id, summary, bill_title, bill_alias, wiki_link, full_text_link) "
                        f"values(:bill_id, :summary, :bill_title, :bill_alias, :wiki_link, :full_text_link)")
        query = query.bindparams(bill_id=bill_id, summary=summary, bill_title=bill_title, bill_alias=bill_alias,
                                 wiki_link=wiki_link, full_text_link=full_text_link)
        conn.execute(query)
        conn.commit()
        conn.close()
