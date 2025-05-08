import sqlite3
import matplotlib.pyplot as plt

def grafik_goster():
    conn = sqlite3.connect('giderler.db')
    cursor = conn.cursor()
    cursor.execute("SELECT kategori, SUM(miktar) FROM harcamalar GROUP BY kategori")
    veriler = cursor.fetchall()

    kategoriler = [row[0] for row in veriler]
    miktarlar = [row[1] for row in veriler]

    plt.pie(miktarlar, labels=kategoriler, autopct='%1.1f%%')
    plt.title("Kategori Bazinda Harcama Dağilimi")
    plt.show()