import pandas as pd
#pandas has its own accessor operators, loc and iloc
#index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
file=pd.read_csv("Pandas\ds_salaries.csv")
print(file.iloc[0])#To select the first row of data in a DataFrame
#Both loc and iloc are row-first, column-second.
print(file.iloc[:,0])#to print all values of 1st column
print(file.iloc[:3,0])#to print 1st, 2nd & 3rd rows of 1st column
print(file.iloc[1:3,0])#to print only 2nd & 3rd rows of 1st column
print(file.iloc[[0,1,2],0])#to print a list of 1st column
print(file.iloc[-5:])#to print last 5 rows of 1st column
#loc operator: label-based selection. In this paradigm, it's the data index value
print(file.loc[0,"job_title"])
print(file.loc[:,["work_year","job_title","company_size"]])
#loc and iloc operators indexing is almost same except one thing.
#loc count all of the indices whereas iloc count 1 less
#in [0:1000], iloc will print 0-999 but loc will print 0-1000
print(file.loc[file.experience_level=="MI"])#will show locations of MI
print(file.loc[(file.experience_level == 'MI') & (file.employment_type == "CT")])
print(file.loc[(file.experience_level == 'MI') | (file.employment_type == "CT")])
#isin is pandas built in function which allows print values that are in the list
print(file.loc[file.job_title.isin(["ML Enginner","Data Analyst"])])
