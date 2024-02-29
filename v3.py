import psycopg2

conn = psycopg2.connect(database="users",
                        user="postgres",
                        password=1,
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute(""" SELECT * FROM users""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
