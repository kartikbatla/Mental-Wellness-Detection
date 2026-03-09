import sqlite3
import json
from datetime import datetime
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\data")

os.makedirs(DATA_DIR, exist_ok=True)

DB_NAME = os.path.join(DATA_DIR, "mental_wellness.db")

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        journal_text TEXT,
        emotion_distribution TEXT,
        wellness_score INTEGER,
        esi REAL,
        stress_level REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_journal_entry(
    journal_text,
    emotion_distribution,
    wellness_score,
    esi,
    stress_level
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO journal_entries
    (date, journal_text, emotion_distribution, wellness_score, esi, stress_level)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        journal_text,
        json.dumps(emotion_distribution),
        wellness_score,
        esi,
        stress_level
    ))

    conn.commit()
    conn.close()


def fetch_last_n_days(days=7):
    conn = get_connection()

    query = f"""
    SELECT * FROM journal_entries
    WHERE date >= datetime('now', '-{days} days')
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df
