import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
housing_price=pd.read_csv("Pandas\Machine Learning\House Price India.csv")
print(housing_price.columns)
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
y=housing_price.Price
print(y.head())
features=['number of bedrooms','condition of the house','Area of the house(excluding basement)','Area of the basement']
X=housing_price[features]
print(X.head())
# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
#Of the options listed, 50 is the optimal number of leaves.
#Overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions
#Underfitting: failing to capture relevant patterns, again leading to less accurate predictions.
