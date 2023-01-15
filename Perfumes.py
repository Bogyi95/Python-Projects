
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

conn = sqlite3.connect('perfumy.db')
c = conn.cursor()
#c.execute('''CREATE TABLE perfumy(title TEXT, ml TEXT, price TEXT)''')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
r = requests.get('http://douglas.pl/pl/p/3001004983?variant=843605', headers=headers).text

soup = BeautifulSoup(r, 'lxml')


title = soup.title.text
ml = soup.findAll("div", {"class","product-detail__variant-name"},)
price = soup.findAll("span", {"class","product-price__price"})

print(title)
print(ml[3].text)
print(price[7].text)

new_ml = ml[3].text
new_price = price[7].text

c.execute('''INSERT INTO perfumy VALUES(?,?,?)''', (title, new_ml, new_price))
conn.commit()

df = pd.read_sql_query('''SELECT * FROM perfumy''', conn)
print (df)