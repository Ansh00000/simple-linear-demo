# importing library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# importing datasets
dataset = pd.read_csv('../res/Salary_Data.csv')
x = (dataset.iloc[:, : 1])
y = (dataset.iloc[:, -1])

# splitting dataset into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# applying linear regression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
# visualising training set
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('salary vs experience')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()
# visualising test set
plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('salary vs experience')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()







