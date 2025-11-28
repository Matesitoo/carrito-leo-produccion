import os
from typing import Generator
import psycopg2
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")

def getCursor() -> Generator[psycopg2.extensions.cursor, None, None]:
    conn = psycopg2.connect(
        host="db.uubvpmedekdkzyvhjash.supabase.co",
        database="postgres",
        user="postgres",
        password=passwordDB,
        port=5432,
        sslmode="require"
    )
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()