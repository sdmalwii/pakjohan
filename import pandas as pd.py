import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

alamat = "https://id.wikipedia.org/wiki/One_Piece"

req = Request(alamat)
html = urlopen(req).read()
data = BeautifulSoup(html, 'html.parser')
table = data.find_all('table', {'class': 'wikitable'})[0]

rows = table.findAll('tr')

hasil = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    hasil.append(cols)

df_hasil = pd.DataFrame(hasil)

# Pisahkan kolom 'text' menjadi dua kolom terpisah
split_cols = df_hasil[0].str.split('\n', n=1, expand=True)
if len(split_cols.columns) == 2:
    df_hasil[['text', '1']] = split_cols
else:
    print("Jumlah kolom tidak sesuai. Periksa kembali dataframe Anda.")

df_hasil.drop(0, axis=1, inplace=True)

# Ubah nama kolom jika jumlah kolom sesuai
expected_columns = ['text', '1']
if len(df_hasil.columns) == len(expected_columns):
    df_hasil.columns = expected_columns
else:
    print("Jumlah kolom tidak sesuai. Periksa kembali dataframe Anda.")

df_hasil.to_csv('rawdata.csv', index=False)
