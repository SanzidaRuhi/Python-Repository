import pandas as pd
#A Series is a sequence of data values.
#If a DataFrame is a table, a Series is a list. 
a=pd.Series([1, 2, 3, 4, 5])
print("series:\n",a)
#A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. 
#Series does not have a column name, it only has one overall name
b=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print("series:\n",b)
#The Series and the DataFrame are intimately related. It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". 
ingredients = pd.Series(["4 cups","1 cup","2 large","1 can"],index=["Flour","Milk","Eggs","Spam"],name="Dinner")
print("ingredients series:\n",ingredients)