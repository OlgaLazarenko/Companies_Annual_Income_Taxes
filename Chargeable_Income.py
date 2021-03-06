
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


import csv, os
import pandas as pd  
import numpy as np  





file_path = "E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income.csv"

# create a function to validate the column year_of_assessment,the range: 2007-2018, nulls are not allowed
def validate_year(year_of_assessment) :
    if year_of_assessment.isdigit() :
        if 2007 <= int(year_of_assessment) <= 2018 :
            result_year = True
        else:
            result_year = False
    else:
        result_year = False
    return result_year



# create a function to validate the other columns
# the values should be positive numbers(integers or decimals), nulls are not allowed
def validate_tax_value(tax) : 
    tax = tax.replace('.','') # remove the dot from the value
    tax = tax.replace(',','') # remove the comma from the value
    result_tax = tax.isdigit() # to find out if the value only contains the digits 
    return result_tax # the function will return True or False



data_file_path = 'E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income.csv'
output_file_path = 'E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income_Output.csv'
error_file_path= 'E:\_Python_Projects_Data\Companies_Income_Annual\Chargeable_Income_Errors.csv'


# read the initial data and perform the data validation
with open(data_file_path, 'r') as input_file :
    with open(output_file_path, 'w') as output_file :
        with open(error_file_path, 'w') as error_file :
            header = input_file.readline()

            output_file.write(header) # write the header to the output_file
            error_file.write(header) # write the header to the error_file

            print()

            row_list = [] # list for each row
            text = input_file.readlines()
            for row in text : # row is the string type
                # convert comma-delimited string to the list
                row_list = row.split(',')


                # call the function 'validate_year(year_of_assessment)' 
                result_year = validate_year(row_list[0])
                if result_year == True :
                    continue # move the row for the next step of validation
                else :
                    error_file.write(row)



                # call the function "validate_tax_value(tax)"
                for n in range(0,13) :
                    result_tax = validate_tax_value(row_list[n])
                    if result_tax == True :
                        continue
                    else:
                        error_file.write(row)

                # validate the last column's values

                result_tax = validate_tax_value(row_list[13])
                if result_tax == True :
                    output_file.write(row)
                else :
                    error_file.write(row)

                
print('The output file:')

with open(output_file, 'r') as good_data :
    text = good_data.readlines()
    print(text)



            
'''
            line_count = 0
            for line in input_file :
                if line_count == 0 : # the header
                    header = line
                    print('*****************')
                    print(header)
                    print('*****************')
                    
                    output_writer.writerow(header) # write the header to the output file
                    error_writer.writerow(header) # write the header to the errors file
                    line_count += 1

                print(line, end = '')
            
            

    
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

# sort data by the column year_of_assessment

df = df.sort_values(by = 'year_of_assessment', ascending = True)
print(df)


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
















