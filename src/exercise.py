import os
import connection
import psycopg2
import pandas as pd

conn = connection.connect()
cursor = conn.cursor()
# cursor.execute('SELECT * FROM Movies')

df = pd.read_sql('SELECT * FROM Movies', conn)
print(df)
conn.close()
