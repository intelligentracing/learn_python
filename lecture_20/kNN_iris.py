## This is course material for Introduction to Python Scientific Programming
## Class 20 Example code: kNN_iris.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# Prepare the training and testing data
X, l = load_iris(return_X_y = True)
X_train, X_test, l_train, l_test = train_test_split(X, l, test_size = 0.5)

# Create kNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, l_train)

# classify 
l_result = knn.predict(X_test)
print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))