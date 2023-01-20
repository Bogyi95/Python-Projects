import requests
from tkinter import *
from tkinter import ttk

#####################################GUI####################################################
#tworzenie okna aplikacji
root = Tk()
root.title("Currencry Converter")
root.geometry("300x300")

#tworzenie boxow do wpisywania
currencyFrom = Entry(root, width=35, borderwidth=5) 
currencyTo = Entry(root,width=35, borderwidth=5)
wynik = Entry(root,width=35,borderwidth=5)
#tworzenie przycisku
przycisk = Button(root, text="Convert")
#wrzucanie boxow i przycisku do okna
currencyFrom.pack(pady=20)
currencyTo.pack()
przycisk.pack()
wynik.pack()

root.mainloop()

##############################################################################################

from_currency = str(input("Enter in the currency you'd like to exchange from: ")).upper()

to_currency = str(input("Enter in the currency  you'd like to exchange to: ")).upper()

amount = float(input("Enter in the amout of money: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")

###################################################################################################