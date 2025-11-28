import os
from typing import Generator
import psycopg2
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")

def getCursor() -> Generator[psycopg2.extensions.cursor, None, None]:
    try:
        print(f"Attempting connection with password: {passwordDB[:5]}...")  # Debug
        
        conn = psycopg2.connect(
            host="db.uubvpnmdekdkzyvhjasb.supabase.co",
            database="postgres",
            user="postgres",
            password=passwordDB,
            port=5432,
            sslmode="require",
            connect_timeout=10
        )
        print("Database connection successful!")
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
        print(f"Database connection failed: {str(e)}")
        raise