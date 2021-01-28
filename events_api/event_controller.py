from db import get_db

def insert_event(name, location, start_timestamp, end_timestamp):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO events(name, location, start_timestamp, end_timestamp) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [name, location, start_timestamp, end_timestamp])
    db.commit()
    return cursor.rowcount

def insert_user(email, name):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(email, name) VALUES (?, ?)"
    cursor.execute(statement, [email, name])
    db.commit()
    return cursor.rowcount

def event_signup(event_uid, email):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO signed_events (event_uid, email) VALUES (?,?)"
    cursor.execute(statement, [event_uid, email])
    db.commit()
    return cursor.rowcount

def event_unsign(event_uid, email):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM signed_events WHERE event_uid = ? AND email = ?"
    cursor.execute(statement, [event_uid, email])
    db.commit()
    return cursor.rowcount

def update_game(id, name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_events():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT json_object('event_uid', event_uid, 'name', name, 'location', location, 'start_timestamp', start_timestamp, 'end_timestamp', end_timestamp) FROM events"
    cursor.execute(query)
    return cursor.fetchall()

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT json_object('email', email, 'name', name) FROM users"
    cursor.execute(query)
    return cursor.fetchall()

def get_event_users(event_uid):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT json_object('event_uid', event_uid, 'email', email) FROM signed_events WHERE event_uid = ?"
    cursor.execute(query, [event_uid])
    return cursor.fetchall()

def get_event_info(event_uid):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT json_object('event_uid', event_uid, 'name', name, 'location', location, 'start_timestamp', start_timestamp, 'end_timestamp', end_timestamp) FROM events WHERE event_uid = ?"
    cursor.execute(query, [event_uid])
    return cursor.fetchall()

def get_user_info(email):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT json_object('email', email, 'name', name) FROM users WHERE email = ?"
    cursor.execute(query, [email])
    return cursor.fetchall()
