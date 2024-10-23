'''
price
year
KMS
Engine


model / make
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge,LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

car=pd.read_csv('cars_details.csv')
#print(car.info())
x=car[['Kilometer','Year']]
y=car[['Price']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)
model=LinearRegression()
model.fit(x_train,y_train)

model2=Ridge(alpha=200.0)  #regularization strength
model2.fit(x_train,y_train)
y_predict=model.predict(x_test)
y1_predict=model2.predict(x_test)

print(root_mean_squared_error(y_test,y_predict))
print(root_mean_squared_error(y_test,y1_predict))

#print(x_test['Kilometer'])
plt.scatter(x_test['Year'],y_test)
plt.scatter(x_test['Year'],y_predict,color='red')
plt.scatter(x_test['Year'],y1_predict,color='green')
#plt.xlim(5000)
plt.ylim(600000)
plt.show()