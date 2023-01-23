import requests
from tkinter import *
from tkinter import ttk

result = ''
def convert():
    
    from_currency = currency_from_var.get()
    to_currency = currency_to_var.get()
    amount = amount_to_convert.get()
    response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
    result = response.json()['rates'][to_currency]
    result_label.config(text=result)

#####################################GUI####################################################
#creating the window
root = Tk()
root.title("Currency Converter")
root.geometry("300x300")


#creating entry to enter the amount to convert 
amount_to_convert = ttk.Entry(root, width=15)
amount_to_convert.pack(pady=5)

#creating drop-down menu
currency_from_var = StringVar(root)
currency_from_var.set("USD")
dropdown_from = OptionMenu(root, currency_from_var, "USD", "PLN", "EUR")
dropdown_from.pack()


#drop down menu 
currency_to_var = StringVar(root)
currency_to_var.set("PLN")
dropdown_to = OptionMenu(root, currency_to_var, "USD", "PLN", "EUR")
dropdown_to.pack()

#creating convert button
przycisk = ttk.Button(root, text="Convert", command=convert)
przycisk.pack()

#displaying the result as label
result_label = Label(root, text=result)
result_label.pack()

#this is for the window to not close unless the loop is broken
root.mainloop()
 
