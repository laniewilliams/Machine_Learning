''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd

db = datasets.load_diabetes()
#how many sameples and How many features?
print(db.data.shape)
#442 Samples
#10 Features

# What does feature s6 represent?

#print(db.DESCR)
# Blood Sugar Level

#print out the coefficient
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target, random_state=11)
lr = LinearRegression()

lr.fit(X_train, y_train) #this is where the learning is taking place

print(lr.coef_)


#print out the intercept

print(lr.intercept_)


# create a scatterplot with regression line


predict = lambda x: x*lr.coef_ + lr.intercept_
predicted = lr.predict(X_test)
#plt.scatter(X_test, y_test, color ='b')
plt.plot(y_test, predicted, '.')


plt.show()