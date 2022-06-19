from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

def connect():
    conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
    return conn
