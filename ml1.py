from sklearn.datasets import load_digits

digits = load_digits()

#print(digits.data[:2])

#print(digits.data.shape)

#print(digits.target[:2]) #saying that these set of numbers belong to the number ZERO
#print(digits.target.shape) # has just one column which is the answer between (0,9) - nothing showing up means one column

#print(digits.images[:2]) #creates a 2-D array, but cannot be used in the model because ethe model needs a 1-D array

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))

for item in zip(axes.ravel(), digits.images, digits.target): #zip helps us iterate it together instead of separately
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r) #using a grey scale, taking the image and putting it in the figures
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
#plt.show()

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(digits.data, digits.target,random_state=11)

print(data_train.shape) #training the data --> 2-D
print(data_test.shape)
print(target_train.shape) # just going to 1-D
print(target_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X=data_train , y=target_train)  #it all comes down to this one method. this will do all of the machine learning. 
                                        #It needs the data (what it should look at) and the target (what it should be)

predicted = knn.predict(X=data_test) #only have X because you don't need the target because it will tell you the target

#how do we know if it's correct?
expected = target_test

print(predicted[:20])
print(expected[:20])

print(format(knn.score(data_test,target_test),".2%")) #lets us see how accurate they are

#how many did they get wrong?

wrong = [(p,e)for (p,e) in zip(predicted,expected) if p != e] #put in the wrongs as a tuple in a list called wrong
print(wrong)

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion) #allows you the see where it kind of messed up. 