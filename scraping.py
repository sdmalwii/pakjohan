#py -m pip install beautifulsoup4
#py -m pip install nltk
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

alamat = "https://id.wikipedia.org/wiki/One_Piece"
#alamat = "https://www.detik.com/terpopuler/news"

req = Request(alamat)

html = urlopen(req).read()
data = BeautifulSoup(html, 'html.parser')
table = data.find_all('table', {'class': 'wikitable'})[0]
                                
print(table)         

rows = table.findAll('tr')

hasil = []
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        first_cell = cols[0].text.strip()
        hasil.append(first_cell)
    #cols = [ele.text.strip() for ele in cols]
    #hasil.append(cols)

df_hasil = pd.DataFrame(hasil)

new_headers = ['text']
df_hasil.columns = new_headers

df_hasil.to_csv(r'rawdata.csv', index=False)
#df_hasil.to_csv(r'D:\openapi\rawdata.csv', index=False)

#df_hasil