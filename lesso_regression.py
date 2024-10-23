import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import root_mean_squared_error
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

california=fetch_california_housing()

X=california.data
Y=california.target

print(X)
print('********',Y)