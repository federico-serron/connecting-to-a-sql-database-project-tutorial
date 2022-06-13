# importing the reusable functions
# We created the "connect" function on the file reusable_functions.py
# and we are going to use it every time we want to connect to the database
# from reusable_functions import connect, run_file, run_query
# importing pandas
import pandas as pd
import psycopg2

# # 1) Connect to the database here using the SQLAlchemy's create_engine function
"""conn = psycopg2.connect(dbname='dcav0e27is34ob',
                        user='cvxaolswbkucpe',password='0fdccfd33bb9e0f8c5e8cee5a27112b425e72e98c48b1aa906ca6b0a052a3dc1',host='ec2-3-248-121-12.eu-west-1.compute.amazonaws.com', port=5432)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Movies(id INT NOT NULL PRIMARY KEY, title VARCHAR(30) NOT NULL, rating INT);")
conn.commit()

conn.close()"""

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
"""conn = psycopg2.connect(dbname='dcav0e27is34ob',
                        user='cvxaolswbkucpe',password='0fdccfd33bb9e0f8c5e8cee5a27112b425e72e98c48b1aa906ca6b0a052a3dc1',host='ec2-3-248-121-12.eu-west-1.compute.amazonaws.com', port=5432)

cursor = conn.cursor()
cursor.execute("INSERT INTO Movies (id, title, rating) VALUES (2,'Spiderman 2', 5);")
conn.commit()
conn.close()"""


# 4) Use pandas to print one of the tables as dataframes using read_sql function
conn = psycopg2.connect(dbname='dcav0e27is34ob',
                        user='cvxaolswbkucpe',password='0fdccfd33bb9e0f8c5e8cee5a27112b425e72e98c48b1aa906ca6b0a052a3dc1',host='ec2-3-248-121-12.eu-west-1.compute.amazonaws.com', port=5432)

cursor = conn.cursor()
pd.read_sql('SELECT * FROM Movies', conn)

conn.close()