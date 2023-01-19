import requests
from bs4 import BeautifulSoup

print("Currency converter PLN>USD")
url = 'https://www.bankier.pl/waluty/kursy-walut/forex/USDPLN'

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')


kurs = soup.find("div", {"class","profilLast"}).text.strip()
print(kurs)

iloscPLN = input("Podaj ilosc PLN: ")
iloscUSD = float(iloscPLN) * int(kurs)

print(round(iloscUSD, 2))
