<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
=======
#Rozbuduje go o inne waluty , interface i wyciagne ze strony dokladne kursy na wszystkie waluty
>>>>>>> e200a3758b9ab314de5aa8a0dd6c13955c3f7c9e

print("Currency converter PLN>USD")
url = 'https://www.bankier.pl/waluty/kursy-walut/forex/USDPLN'

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')


kurs = soup.find("div", {"class","profilLast"}).text.strip()
print(kurs)

iloscPLN = input("Podaj ilosc PLN: ")
iloscUSD = float(iloscPLN) * int(kurs)

print(round(iloscUSD, 2))
