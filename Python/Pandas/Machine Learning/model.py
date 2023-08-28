import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
housing_price=pd.read_csv("Pandas\Machine Learning\House Price India.csv")
print(housing_price.describe())
print(housing_price.columns)
housing_price=housing_price.dropna()
print(housing_price)
#selecting predicting target
y=housing_price.Price
print(y)
#choosing features to predict target
features=['number of bedrooms','condition of the house','Area of the house(excluding basement)','Area of the basement']
x=housing_price[features]
print(x.describe())
print(x.head(10))
#Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.
'''The steps to building and using a model are:
Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
Fit: Capture patterns from provided data. This is the heart of modeling.
Predict: Just what it sounds like
Evaluate: Determine how accurate the model's predictions are.'''
## Define model. Specify a number for random_state to ensure same results each run
house_model=DecisionTreeRegressor(random_state=1)
#Specifying a number for random_state ensures you get the same results in each run.
house_model.fit(x,y)#fit model
print("Making predictions prices for the following 5 houses:\n")
print(x.head())
print("The predictions prices are:\n")
print(house_model.predict(x.head()))
print(y.head())
#Mean Absolute Error (also called MAE) a metric for summarizing model quality
#The prediction error for each house is: error=actual-predicted
'''With the MAE metric, we take the absolute value of each error. 
This converts each error to a positive number. 
We then take the average of those absolute errors. 
This is our measure of model quality.'''
predicted_house_price=house_model.predict(x)
print(mean_absolute_error(y,predicted_house_price))
'''The scikit-learn library has a function train_test_split to break up the data into two pieces. 
split data into training and validation data, for both features and target
The split is based on a random number generator. 
Supplying a numeric value to the random_state argument guarantees we get the same split every time we run this script.'''
train_X, val_X, train_y, val_y = train_test_split(x, y, random_state = 0)
house_model=DecisionTreeRegressor()## Define model
house_model.fit(train_X,train_y)## Fit model
# get predicted prices on validation data
val_predictions = house_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))