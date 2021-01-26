import sqlite3
DATABASE_NAME = "events_api.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn


def create_event():
    tables = [
        """CREATE TABLE IF NOT EXISTS events(
                event_uid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				location REAL NOT NULL,
				start_timestamp INTEGER NOT NULL,
                end_timestamp INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def create_user():
    tables = [
        """CREATE TABLE IF NOT EXISTS users(
                email TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def signed_events():
    tables = [
        """CREATE TABLE IF NOT EXISTS signed_events(
                event_uid INTEGER NOT NULL,
                email TEXT NOT NULL,
                PRIMARY KEY (event_uid, email)
                FOREIGN KEY (email) REFERENCES users(email)
                FOREIGN KEY (event_uid) REFERENCES events (event_uid)
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
