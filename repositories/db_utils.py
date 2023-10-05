import os

import sqlalchemy


def get_connection():
    return sqlalchemy.create_engine(os.getenv("LINODE_CONN_STRING")).connect()