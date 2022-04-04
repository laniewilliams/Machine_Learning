from sklearn.datasets import load_digits

digits = load_digits()

print(digits.data[:2])

print(digits.data.shape)

print(digits.target[:2]) #saying that these set of numbers belong to the number ZERO
print(digits.target.shape) # has just one column which is the answer between (0,9) - nothing showing up means one column

print(digits.images[:2]) #creates a 2-D array, but cannot be used in the model because ethe model needs a 1-D array

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))

for item in zip(axes.ravel(), digits.images, digits.target): #zip helps us iterate it together instead of separately
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r) #using a grey scale, taking the image and putting it in the figures
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
plt.show()