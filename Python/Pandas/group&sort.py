import pandas as pd
file=pd.read_csv("Pandas\ds_salaries.csv")
pd.set_option("display.max_rows", 5)
print(file.groupby('salary').salary.count())
#groupby() created a group of reviews which allotted the same salary values
#Then, for each of these groups, we grabbed the salary() column and counted how many times it appeared. 
#value_counts() is just a shortcut to this groupby() operation.
print(file.groupby('salary_in_usd').salary.min())
print(file.groupby('employment_type').apply(lambda df: df.job_title.iloc[0]))
print(file.groupby(['job_title', 'experience_level']).apply(lambda df: df.loc[df.salary.idxmax()]))
print(file.groupby(['job_title', 'employment_type']).apply(lambda df: df.loc[df.salary.idxmax()]))
print(file.groupby(['job_title', 'employment_type','employment_type']).apply(lambda df: df.loc[df.salary.idxmax()]))
#Another groupby() method agg() lets you run a bunch of different functions on your DataFrame simultaneously
print(file.groupby(['job_title']).salary.agg([len, min, max]))
#multi-index differs from a regular index in that it has multiple levels.
title_reviewed = file.groupby(['job_title','employment_type', 'experience_level']).salary.agg([len])
print(title_reviewed)
print(type(title_reviewed.index))
a=title_reviewed.reset_index()
print(a)
print(a.sort_values(by='len'))#sort in ascending order
print(a.sort_values(by='len',ascending=False))#sort in descending order
print(a.sort_index())
print(a.sort_values(by=['job_title','len']))
print(a.sort_values(by=['len','job_title']))
#sorting works using 1st requirement and then goes for 2nd requirement