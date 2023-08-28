import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
#The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree.
#random forest generally has much better predictive accuracy than a single decision tree and it works well with default parameters.
housing_price=pd.read_csv("Pandas\Machine Learning\House Price India.csv")
print(housing_price.columns)
y=housing_price.Price
print(y.head())
features=['number of bedrooms','condition of the house','Area of the house(excluding basement)','Area of the basement']
X=housing_price[features]
print(X.head())
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
house_predict = forest_model.predict(val_X)
print(mean_absolute_error(val_y, house_predict))