import mysql.connector

# Membuat koneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="walid"
)

# Membuat objek cursor
cursor = conn.cursor()

# Menjalankan query untuk mendapatkan data
query = "SELECT * FROM mahasiswa"
cursor.execute(query)

# Mengambil semua baris hasil query
rows = cursor.fetchall()

# Menampilkan data
for row in rows:
    print(row)

# Menutup cursor dan koneksi
cursor.close()
conn.close()