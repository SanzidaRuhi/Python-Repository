import pandas as pd
#DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.
data=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
#We are using the pd.DataFrame() constructor to generate these DataFrame objects. The syntax for declaring a new one is a dictionary whose keys are the column names and whose values are a list of entries. 
print("dataframe: \n",data)
data=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.'], 'rad': ['alright','quite ok']})
print("dataframe: \n",data)
data=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.'],
              'rad': ['alright','quite ok']},
             index=['Product A:', 'Product B:'])
#The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor
print("dataframe: \n",data)
fruits = pd.DataFrame({"Apples":[30],"Bananas":[21]})
print("fruits:\n",fruits)
fruit_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=["2017 Sales","2018 Sales"])
print("fruit_sales:\n",fruit_sales)
#The isnull() and notnull() functions in pandas are used to check for missing or null values in a DataFrame or Series.
#The isnull() function returns a Boolean mask indicating where values are missing or null. 
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, None, 40],
    'Gender': ['Female', 'Male', None, 'Male']
}
df = pd.DataFrame(data)
print(df.isnull())
#The notnull() function returns a Boolean mask indicating where values are not missing or null. 
print(df.notnull())