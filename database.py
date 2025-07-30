import sqlite3

def init_db():
    conn = sqlite3.connect("resume.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_score(name, score):
    conn = sqlite3.connect("resume.db")
    c = conn.cursor()
    c.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()
