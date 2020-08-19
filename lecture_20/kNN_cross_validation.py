## This is course material for Introduction to Python Scientific Programming
## Class 20 Example code: kNN_cross_validation.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np

# Prepare the training and testing data
X, l = load_iris(return_X_y = True)
X_train, X_test, l_train, l_test = train_test_split(X, l, test_size = 0.75)

# Prepare cross-validation set
kfold = KFold(n_splits = 5)
kfold.get_n_splits(X_train)

highest_validation = 0
for k in range(1, 6):
    knn = KNeighborsClassifier(n_neighbors = k)
    accuracy = 0
    for training_index, validation_index in kfold.split(X_train):
        X_kfold_train = X_train[training_index]
        l_kfold_train = l_train[training_index]
        X_kfold_validation = X_train[validation_index]
        l_kfold_validation = l_train[validation_index]

        knn.fit(X_kfold_train, l_kfold_train)
        l_validation_result = knn.predict(X_kfold_validation)
        accuracy += np.sum(l_validation_result == l_kfold_validation)/len(l_kfold_validation)
    
    if accuracy > highest_validation:
        highest_validation = accuracy
        best_k = k
print('Through cross validation, optimal k = ', best_k)        

# Create kNN classifier
knn = KNeighborsClassifier(n_neighbors = best_k)
knn.fit(X_train, l_train)

# classify 
l_result = knn.predict(X_test)
print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))