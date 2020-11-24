
#!/bin/python3
'''
Project Name: Companies Annual Chargeable_Income (2007-2018)
Part 1: Chargeable_Income
Date: Nov 22, 2020
Author: Olga Lazarenko
Description: 


The data file has the columns:
1) year_of_assessment  *
2) no_of_companies_assessed *
3) total_income  *
4) donations
5) chargeable_income *
6) group_relif
7) loss_carryback_relief
8) ci_alt_reliefs
9) tax_exemptions
10) ci_aft_examptions
11) gross_tax_payable 
12) tax_deducted_at_source
13) other_tax_set_offs
14) net_tax_assessed  * 

Create calculated fields:
- % change of the number of the companies assessed over the time 
- % change of total income over the time
- average income per company = income/no_of_companies
- % change of the avg income/company
- % change of the chargeable income over time (because the tax rates can be diffrent for every year)
- 
- 

Additional:
1) Find the data about yearly taxes for US companies
2) Find the data about tax relief over the time
3) Find the data about tax examptions



'''



import pandas as pd  
import numpy as np  



df = pd.read_csv('E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income.csv', 
                    usecols = 
                    [
                        'year_of_assessment', 'no_of_companies_assessed', 'total_income', 'donations'
                        ,'chargeable_income', 'tax_exemption','net_tax_assessed'
                    ])

print()
print(df)
print('-----------------------------------------------------------------')


# remove rows with year_of_assessment duplicates
df.drop_duplicates(subset = "year_of_assessment",
                            keep = 'first', # keep the first duplicate,
                            inplace = True)

print(df)
print('____________________________________________________________________')
'''
# to validate the year_of_assessment, apply to this column
print(df['year_of_assessment'])



 # or item in df['year_of_assessment'] :
# create a function to validate year_of_assessment

print()
print('--------------')
def year_validation(year_value) :
    if year_value >= 2007 and year_value <= 2018 :
        result = "True"   
    else:
        result = "False"
    return result
        

df['year_of_assessment'] = df['year_of_assessment'].apply(lambda x: year_validation(x))
# print(df['year_of_assessment'])
'''

















