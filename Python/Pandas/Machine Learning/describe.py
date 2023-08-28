import pandas as pd
import sklearn
housing_price=pd.read_csv("Pandas\Machine Learning\House Price India.csv")
print(housing_price.describe())#this function will show various results of the file
#The results show 8 numbers for each column in your original dataset. 
#count shows how many rows have non-missing values.
#mean, which is the average.
#std is the standard deviation, which measures how numerically spread out the values are.
#To interpret the min, 25%, 50%, 75% and max values, imagine sorting each column from lowest to highest value. 
#The first (smallest) value is the min. 
#If you go a quarter way through the list, you'll find a number that is bigger than 25% of the values and smaller than 75% of the values.
#The 50th and 75th percentiles are defined analogously
#max is the largest number.
print(housing_price.columns)#will print columns and its type
housing_price=housing_price.dropna()# dropna drops missing values (think of na as "not available")
print(housing_price)
print(sklearn.__version__)#checking sklearn version