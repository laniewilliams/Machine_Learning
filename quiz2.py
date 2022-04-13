import pandas as pd
from sklearn.model_selection import train_test_split
animal_class = pd.read_csv('animal_classes.csv') #reading the csv directly into the dataframe
animal_test = pd.read_csv('animals_test.csv')
animal_train = pd.read_csv('animals_train.csv')
#print(animal_class.head(3)) #date is the data and temperature is the target
#print(animal_test.head(5))
#print(animal_train.head(5))

X_train = animal_train.iloc[:,0:16].to_numpy()
y_train = animal_train.class_number.values.reshape(-1,1)
X_test = animal_test.iloc[:,1:17].to_numpy()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X=X_train , y=y_train)  #it all comes down to this one method. this will do all of the machine learning. 
                                        #It needs the data (what it should look at) and the target (what it should be)

predicted = knn.predict(X=X_test) #only have X because you don't need the target because it will tell you the target
