import pandas as pd
import mysql.connector
from mysql.connector import Error

# Fungsi untuk membuat koneksi ke database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='db_openapi',
            user='root',
            password=''
        )
        if connection.is_connected():
            print('Terhubung ke MySQL Server')
            return connection
    except Error as e:
        print('Error saat menghubungkan ke MySQL:', e)

# Fungsi untuk memasukkan data dari CSV ke MySQL
def insert_data_from_csv(connection, csv_file, table_name):
    try:
        # Baca data dari CSV ke DataFrame
        df = pd.read_csv(csv_file)
        
        # Buat kursor
        cursor = connection.cursor()

        # Hapus tabel jika sudah ada sebelumnya
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        # Buat tabel baru dengan skema yang sesuai dengan DataFrame
        create_table_query = f"CREATE TABLE {table_name} ({','.join([f'{col} TEXT' for col in df.columns])})"
        cursor.execute(create_table_query)

        # Iterasi DataFrame dan masukkan setiap baris ke tabel
        insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s' for _ in range(len(df.columns))])})"
        for row in df.itertuples(index=False):
            cursor.execute(insert_query, row)

        # Commit perubahan ke database
        connection.commit()

        # Tutup kursor
        cursor.close()

        print('Data berhasil dimasukkan ke MySQL.')
    except Error as e:
        print('Error saat memasukkan data ke MySQL:', e)

# Panggil fungsi untuk membuat koneksi
connection = create_connection()

# Memasukkan data dari CSV ke MySQL
insert_data_from_csv(connection,'clean.csv','tbl_api')

# Tutup koneksi
connection.close()