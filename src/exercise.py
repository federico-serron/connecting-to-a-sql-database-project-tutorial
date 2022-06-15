import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv()
print(os.getenv('DB_USER'))
conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))

cursor = conn.cursor()
# cursor.execute('SELECT * FROM Movies')

df = pd.read_sql('SELECT * FROM Movies', conn)
print(df)
conn.close()
