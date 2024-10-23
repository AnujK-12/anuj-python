import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler

data=load_diabetes()

feature_name=['age','sex','bmi','bp','s1','s2','s3','s4','s5','s6']
df=pd.DataFrame(data.data,columns=feature_name)

df['target']=data.target
x=data.data
y=data.target
'''print(x)
print('*********',y)
print('***************',df)'''

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)

model=ElasticNet(alpha=1,l1_ratio=1.0)
model.fit(x_train,y_train)
m2=ElasticNet(alpha=4,l1_ratio=0.0)
m2.fit(x_train,y_train)

y_pred=model.predict(x_test)
y1_pre=m2.predict(x_test)

print(root_mean_squared_error(y_test,y_pred))

print(x_test.shape)
print('********',y_test.shape)
plt.scatter(x_test[:,0],y_test,color='blue')
plt.scatter(x_test[:,0],y_pred,color='green')
plt.scatter(x_test[:,0],y1_pre,color='red')
plt.show()


'''
std=StandardScalar()
data['age']=std.fit_transform(data['age'])
'''