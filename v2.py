import psycopg2

conn = psycopg2.connect(database="users",
                        user="postgres",
                        password=1,
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute("""
    INSERT INTO users (id,name,email) VALUES
    (1,'Alan Walker','allnc@gmail.com'), 
    (2,'Steve Jobs','sjobs@gmail.com')
  """)
conn.commit()
conn.close()
