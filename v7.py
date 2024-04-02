import psycopg2


def create_table():
    try:
        conn = psycopg2.connect(database="mydatabase",
                                user="postgres",
                                password="your_password",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()  # creating a cursor
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data
        (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """)
        conn.commit()
        print("Table created successfully")
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_table()
