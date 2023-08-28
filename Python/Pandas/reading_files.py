import pandas as pd
#csv file means Comma-Separated Values
#reading from a csv file
file=pd.read_csv("Pandas\ds_salaries.csv")
print("number of rows and coloums: ",file.shape)
print(file.head())#it will print 1st 5 rows as default
print("\nnow print 10 results together")
print(file.head(10))#it will print 1st 10 rows together and we can change the number of printed rows as we want
#writing to a csv file
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)
animals.to_csv("cows_and_goats.csv")
print(file.work_year)#way of accessing columns of csv file
#print(file["work_year"])#we can also access columns of csv file using this way
print(file["work_year"][10])#accessing elements in columns
#file.set_index("title")#set title as a index name
print(file)
print(file.experience_level=="SE")#show if all experince level is se or not
file['index_backwards'] = range(len(file), 0, -1)#indexing reverse
print(file['index_backwards'])
animals['cows'] = 25#change values in indices
print(animals['cows'])