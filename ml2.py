# goal to produce a simple linear regression with predicted and expected values
import pandas as pd
from sklearn.model_selection import train_test_split
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv') #reading the csv directly into the dataframe

print(nyc.head(3)) #date is the data and temperature is the target

#each column in a dataframe is called a series

#we have one column but we need to feed the model 4 different things

print(nyc.Date.values) #this is not in the format that we need it. They have to be separated into rows

print(nyc.Date.values.reshape(-1,1)) #(-1,1) the first arguemnt is the number of rows and the second argument is the number of columns.
                                        #-1 tells it to infer the number of rows based on the data

X_train , X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1,1), nyc.Temperature.values,random_state=11)
 #random_state = 11 is a controlled random. If we don't do random state we won't have the same results as Prof
 # Now, our results will match

print(X_train.shape)
print(X_test.shape)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

'''

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X=X_train, y=y_train) #this is where the learning is taking place

print(lr.coef_)
print(lr.intercept_)

predicted = lr.predict(X_test)

expected = y_test #just changing the name for clarity purpsoses

for p,e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')
#there is so much discrepancy because we only have the year and the temperature, just oen feature

predict = lambda x: x*lr.coef_ + lr.intercept_
print(predict(2025))
print(predict(1890))

import seaborn as sns

axes = sns.scatterplot(data=nyc,x='Date', y='Temperature', hue='Temperature',palette='winter',legend=False)

axes.set_ylim(10,70)

import numpy as np
x = np.array([min(nyc.Date.values),max(nyc.Date.values)]) #to create the regression line we need 4 points (starting x,y and ending x,y)
                #grab the min and max from the data frame and then use teh predict function ot get the y

print(x)
y = predict(x)
print(y)

import matplotlib.pyplot as plt

line = plt.plot(x,y) #put in the 4 points
plt.show()
'''