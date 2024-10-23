# give multiple input for x and see diference 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge,LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

x=np.random.rand(100,1)*10
#y= 3+2*x+ np.random.randn(100,1)*2

#polynomial fearure

y=5*x**2+7*x+ np.random.randn(100,1)*5 
poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30)
model=LinearRegression()
model.fit(x_train,y_train)

model2=Ridge(alpha=200.0)  #regularization strength
model2.fit(x_train,y_train)
y_predict=model.predict(x_test)
y1_predict=model2.predict(x_test)

print(root_mean_squared_error(y_test,y_predict))
print(root_mean_squared_error(y_test,y1_predict))

plt.scatter(x_test,y_test,color='blue')
plt.scatter(x_test,y_predict,color='red')
plt.scatter(x_test,y1_predict,color='green')

plt.scatter(x,y)
plt.show()


