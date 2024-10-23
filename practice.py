import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
laptop= pd.read_csv('Laptop_price.csv')
print(laptop)

def eda(d):
  print(d.head().to_string())
  print("**************")
  print(d.tail().to_string())
  print("**************")
  print(d.info())
  print("**************")
  print(d.describe())
  print("**************")
  print(d.isnull().sum())
  print("**************")
  print(d.shape)
  print("**************")
  print(d.dtypes)

eda(laptop)

'''
Brand ,Processor_Speed,Storage_Capacity


Price
'''

x=laptop[['Processor_Speed','Storage_Capacity','RAM_Size']]
y=laptop['Price']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=50)


model=linear_model.LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

plt.scatter(x_test['Storage_Capacity'],y_test,color='red')
#plt.scatter(x_test['RAM_Size'],y_test,color='red')
plt.plot(x_test['Storage_Capacity'],y_pred,color='green',)
plt.grid()


def user_input():
    try:
        speed=float(input('Enter speed required'))
        storage=int(input('Enter required storage'))
        size=int(input('Enter size'))

        uinput=pd.DataFrame([[speed,storage,size]])
        upred=model.predict(uinput)
        print('Price is ',upred)
        print(uinput)

        plt.scatter(uinput[1],upred[0],color='yellow')
    except ValueError:
       print('Invalid Input')

user_input()

plt.show()