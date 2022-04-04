from sklearn.datasets import load_digits

digits = load_digits()

print(digits.data[:2])

print(digits.data.shape)

print(digits.target[:2]) #saying that these set of numbers belong to the number ZERO
print(digits.target.shape) # has just one column which is the answer between (0,9) - nothing showing up means one column