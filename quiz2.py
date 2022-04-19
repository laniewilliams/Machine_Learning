import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split

#importing the data
animal_class = pd.read_csv('animal_classes.csv') #reading the csv directly into the dataframe
animal_test = pd.read_csv('animals_test.csv')
animal_train = pd.read_csv('animals_train.csv')

#assigning data to variables
X_train = animal_train.iloc[:,0:16].to_numpy()
y_train = animal_train.class_number.values.reshape(-1)
X_test = animal_test.iloc[:,1:17].to_numpy()

#Training the model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=X_train , y=y_train)  #it all comes down to this one method. this will do all of the machine learning. 
                                        #It needs the data (what it should look at) and the target (what it should be)
predicted = knn.predict(X=X_test) #only have X because you don't need the target because it will tell you the target


#Creating the list of predicted Classes
predicted_list = []
for x in np.nditer(predicted):
    predicted_list.append(animal_class.loc[animal_class['Class_Number']==x,"Class_Type"].values[0])


#Creating the list of animal names
animal_name_list = []
for i in animal_test.index:
    animal_name_list.append(animal_test.animal_name[i])


#writing them to the csv file
with open('predictions.csv','w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['animal_name','prediction'])
    for item in zip(animal_name_list,predicted_list):
        c = csvwriter.writerow(item)



