import psycopg2


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="",
            database="",
            user="",
            password="",
            port=""
        )
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Connected to Postgres database")
        print(f"Database version:{db_version[0]}")

        return conn

    except psycopg2.Error as e:
        print(f"Error connect to PostgreSQL database: {e}")
        return None
    finally:
        if "conn" in locals():
            cursor.close()
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    connection = connect_to_db()
