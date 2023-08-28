#functions & maps
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 5)#this function will show only 5 rows in total
file=pd.read_csv("Pandas\ds_salaries.csv")
print(file)
print(file.salary.describe())
print(file.job_title.describe())
print(file.job_title.unique())#shows unique values
print(file.job_title.value_counts())#shows how many times a value occurs
#A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values
file_salary_mean=file.salary.mean()
print(file_salary_mean)
print(file_salary_mean-file.salary)
print(file.salary.map(lambda p : p - file_salary_mean))
#The function pass to map() should expect a single value from the Series (a salary value, in the above example), and return a transformed version of that value.
#map() returns a new Series where all the values have been transformed by your function.
def remean_salary(row):
    row.salary = row.salary - file_salary_mean
    return row
print(file.apply(remean_salary, axis='columns'))
#apply() is an another way to map
#If we had called reviews.apply() with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.
print(file.experience_level+" - "+file.employment_type)
median_salary = file.salary.median()
print(median_salary)