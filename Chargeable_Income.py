
#!/bin/python3
'''
Project Name: Companies Annual Chargeable_Income
Part 1: Chargeable_Income
Date: Nov 22, 2020
Author: Olga Lazarenko
Description: 
'''

print('Hello Olga!')

import pandas as pd
import numpy as np

df = pd.read_csv('E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income.csv')
print(df)

df = pd.read_csv('E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income.csv', usecols = ['year_of_assessment'])
print(df)










