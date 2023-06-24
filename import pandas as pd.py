import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

alamat = "https://id.wikipedia.org/wiki/One_Piece"
req = Request(alamat)

html = urlopen(req).read()
data = BeautifulSoup(html, 'html.parser')
table = data.find_all('table', {'class': 'wikitable'})[0]
                                
print(table)         

rows = table.findAll('tr')

hasil = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    hasil.append(cols)

df_hasil = pd.DataFrame(hasil)
#df_hasil
df_hasil.to_csv(r'C:\Users\nurwa\OneDrive\Desktop\rawdata.csv', index=False)