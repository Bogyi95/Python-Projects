#Rozbuduje go o inne waluty , interface i wyciagne ze strony dokladne kursy na wszystkie waluty

print("Currency converter PLN>USD")

kurs = 4.35

iloscPLN = input("Podaj ilosc PLN: ")
iloscUSD = float(iloscPLN) * kurs

print(round(iloscUSD, 2))
