import pandas as pd
file=pd.read_csv("Pandas\ds_salaries.csv")
print(file)
print(file.salary.dtype)#dtype property shows the type of a specific column.
print(file.dtypes)#dtypes property returns the dtype of every column in the DataFrame
print(file.salary.astype("float32"))#astype convert the type from one to another is possible
print(file.salary.astype("object"))#convert it into object
print(file.index.dtype)
#Pandas provides some methods specific to missing data. To select NaN entries you can use pd.isnull() (or its companion pd.notnull()). 
print(file[pd.isnull(file.employee_residence)])#will show NaN where is missing values
#Replacing missing values is a common operation.
#fillna() provides a few different strategies for mitigating such data. 
print(file.employee_residence.fillna("unknown"))#will replace NaN with unknown
print(file.job_title.replace('ML Engineer','ml engineer'))
#replace function replace the words when finding it