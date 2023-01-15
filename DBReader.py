import sqlite3
import pandas as pd 


conn = sqlite3.connect('perfumy.db')

df = pd.read_sql_query('''SELECT * FROM perfumy''', conn)
print (df)