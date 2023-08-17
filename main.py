import datetime
import json

from flask import Flask, request, redirect
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import sql
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import requests
import logging
from statsmodels.tsa.arima.model import ARIMA
import cachetools
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# create console logger and file logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler1)
handler2 = logging.FileHandler('crypto-opportunity-service.txt')
handler2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler2)

app = Flask(__name__, static_folder='crypto-opportunity-front-end/dist', static_url_path='')
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["300 per hour", "30 per minute"],
    storage_uri="memory://",
)
CORS(app)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/ira-q-and-a')
def ira_q_and_a():
    conn = get_connection()
    df = pd.read_sql(sql.text("SELECT * FROM ira_questions_and_answers"), conn)
    return df.to_json(orient="records")


def get_connection():
    return sqlalchemy.create_engine(os.getenv("SUPABASE_CONN_STRING")).connect()

