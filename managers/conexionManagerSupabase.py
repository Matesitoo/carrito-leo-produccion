import os
from typing import Generator
import psycopg2
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")

def getCursor() -> Generator[psycopg2.extensions.cursor, None, None]:
    try:
        conn = psycopg2.connect(
            host="aws-0-us-west-1.pooler.supabase.com",
            database="postgres",
            user="postgres.uubvpmedekdkzyvhjash",
            password=passwordDB,
            port=6543,
            sslmode="require",
            connect_timeout=10
        )
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        raise