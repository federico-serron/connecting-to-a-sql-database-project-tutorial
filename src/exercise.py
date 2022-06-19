import os
import connection
import pandas as pd

conn = connection.connect()
cursor = conn.cursor()


# CREATE TABLES
# cursor.execute("""CREATE TABLE sports(
#                 id INT NOT NULL,
#                 name VARCHAR(20),
#                 category VARCHAR(20),
#                 PRIMARY KEY (id))
#                 ;""")

# INSERT DATA
# cursor.execute("""INSERT INTO sports(
#                 id, name, category) VALUES (1, 'Taekwondo', 'Combate')
#                 ;""")




df = pd.read_sql('SELECT * FROM sports', conn)
print(df)
conn.close()
