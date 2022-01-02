import numpy as np
import pandas as pd


Bank_df_1 = pd.DataFrame ({
'Customer ID': ['1', '2', '3', '4', '5'],
'Customer First Name':['John', 'Karlene', 'Ashley', 'Derill', 'Aldrin'],
'Customer Last Name': ['Dale', 'Kapush', 'Smith', 'Doe', 'Johnson']
})

#print (Bank_df_1)


Bank_df_2 = pd.DataFrame ({
'Customer ID': ['6', '7', '8', '9', '10'],
'Customer First Name':['Aldred', 'Do', 'Joshua', 'Mac', 'Rivero'],
'Customer Last Name': ['Williamns', 'Brown', 'Jones', 'Garcia', 'Miller']
})

#print (Bank_df_2)

customer_annual = pd.DataFrame ({
'Customer ID': ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
'Customer Annual Salary': [45555, 30000, 10000, 20000, 56000, 53453, 438749, 23445, 12345, 23934]
})

#print (customer_annual)

two_banks_total = pd.concat ([Bank_df_1, Bank_df_2])
#print (two_banks_total)

total = pd.merge (two_banks_total, customer_annual, on='Customer ID')
#print (total)


#ADD a new bank customer
my_bank_info = pd.DataFrame ({
'Customer ID': ['11'],
'Customer First Name': ['Alexander'],
'Customer Last Name': ['Cruz'],
'Customer Annual Salary': [562345]
})

bank_df_all = pd.concat ([total, my_bank_info])
print (bank_df_all)
