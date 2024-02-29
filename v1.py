import psycopg2

conn = psycopg2.connect(database="users",
                        user="postgres",
                        password=1,
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute("""
CREATE TABLE users
(
    id INT   PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()
conn.close()
