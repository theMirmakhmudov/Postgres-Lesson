import psycopg2


class DatabaseManager:
    def __init__(self, database, user, password, host="localhost", port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.conn = psycopg2.connect(database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         host=self.host,
                                         port=self.port)
            print("Connected to database successfully")
        except psycopg2.Error as e:
            print("Error while connecting to PostgreSQL", e)

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data
            (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """)
            self.conn.commit()
            print("Table created successfully")
        except psycopg2.Error as e:
            print("Error while creating table:", e)

    def close_connection(self):
        try:
            self.conn.close()
            print("Connection closed successfully")
        except psycopg2.Error as e:
            print("Error while closing connection:", e)


if __name__ == "__main__":
    db_manager = DatabaseManager(database="mydatabase",
                                 user="postgres",
                                 password="your_password")
    db_manager.connect()
    db_manager.create_table()
    db_manager.close_connection()
