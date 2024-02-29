import psycopg2

conn = psycopg2.connect(database="users",
                        user="postgres",
                        password=1,
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute("""Delete From users WHERE id =5""")

conn.commit()
conn.close()
