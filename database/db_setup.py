import sqlite3

conn = sqlite3.connect("logs.db")
c = conn.cursor()
c.execute('''CREATE TABLE logs (
    id INTEGER PRIMARY KEY,
    input_text TEXT,
    emotion_scores TEXT,
    gibberish_scores TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()
conn.close()
