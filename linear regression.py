import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

X = 2*np.random.rand(100, 1)  # 0 , 1
Y = 4 + 3*X + np.random.randn(100, 1)  # y = mx+b + # -3 3

print("x = ",X)
print("y = ",Y)

# random state is used for suffle
# porpabilictic speration
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=50)

model = linear_model.LinearRegression()
model.fit(X_train,Y_train)

y_prediction=model.predict(X_test)

print("Y Prediction = ",y_prediction)

mse = root_mean_squared_error(Y_test, y_prediction)

print(mse)

# display data in graph
# display data in graph
plt.scatter(X_test, Y_test, color="blue", label="Actual")
plt.scatter(X_test, y_prediction, color="red", label="Predicted")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression: Actual vs Predicted")
plt.legend()
plt.show()

