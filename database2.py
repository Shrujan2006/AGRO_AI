import sqlite3
import datetime

DB_NAME = "agroai.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crop TEXT,
        severity TEXT,
        confidence REAL,
        land_size REAL,
        temperature REAL,
        total_possible_yield REAL,
        reduction_percent REAL,
        yield_loss REAL,
        estimated_yield REAL,
        economic_loss REAL,
        risk_level TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_record(
    crop,
    severity,
    confidence,
    land_size,
    temperature,
    total_possible_yield,
    reduction_percent,
    yield_loss,
    estimated_yield,
    economic_loss,
    risk_level
):
    conn = get_connection()
    cursor = conn.cursor()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO records (
        crop, severity, confidence, land_size,
        temperature,
        total_possible_yield, reduction_percent,
        yield_loss, estimated_yield,
        economic_loss, risk_level, created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        crop, severity, confidence, land_size,
        temperature,
        total_possible_yield, reduction_percent,
        yield_loss, estimated_yield,
        economic_loss, risk_level, current_time
    ))

    conn.commit()
    conn.close()


def fetch_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records ORDER BY id DESC")
    records = cursor.fetchall()

    conn.close()
    return records