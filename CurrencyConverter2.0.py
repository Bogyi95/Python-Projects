import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

result = ''
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'CNY', 'AUD', 'CAD', 'CHF', 'HKD', 'SGD', 'SEK', 'KRW',
              'NOK', 'NZD', 'INR', 'MXN', 'TWD', 'ZAR', 'BRL', 'DKK', 'PLN', 'THB', 'ILS', 'IDR', 'CZK',]

def convert():
    
    from_currency = currency_from_var.get()
    to_currency = currency_to_var.get()
    amount = amount_to_convert.get()
    if from_currency == to_currency:
        messagebox.showerror("Same Currencies", "You have two same currencies selected")
    else:
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
        result = response.json()['rates'][to_currency]
        #result = float(result)
        result_label.config(text=result)

#####################################GUI####################################################
#creating the window
root = Tk()
root.title("Currency Converter")
root.geometry("500x200")
root.iconbitmap("icon.ico")
root.configure(bg='#28aee4')


#creating entry to enter the amount to convert 
amount_to_convert = ttk.Entry(root, width=15, font=(10))
amount_to_convert.grid(row=0, column=0, padx=5, pady=5)

#creating drop-down menu
currency_from_var = StringVar(root)
currency_from_var.set("USD")
dropdown_from = OptionMenu(root, currency_from_var, *currencies)
dropdown_from.grid(row=1, column=0, ipadx=5, ipady=5)


#drop down menu 
currency_to_var = StringVar(root)
currency_to_var.set("PLN")
dropdown_to = OptionMenu(root, currency_to_var, *currencies)
dropdown_to.grid(row=1, column=3, ipadx=5, ipady=5, padx=5, pady=10)

#creating convert button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=2, ipadx=5, ipady=5, padx=5, pady=10)

#displaying the result as label
result_label = Label(root, text=result, font=(18))
result_label.grid(row=0, column=3, )

dropdown_from.configure(bg='#28aee4', width=15)
dropdown_to.configure(bg='#28aee4', width=15)




#this is for the window to not close unless the loop is broken
root.mainloop()
 
