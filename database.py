import sqlite3

def veritabani_baglan():
    conn = sqlite3.connect('giderler.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS harcamalar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kategori TEXT,
            miktar REAL,
            tarih TEXT
        )
    ''')
    conn.commit()
    return conn