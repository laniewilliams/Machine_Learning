from tkinter import N


remainder = lambda num: num % 2
print(remainder(5))

product = lambda x,y: x*y
print(product(2,3))

def testfunct(num):
    print(num)
    return lambda x: x * num

result10 = testfunct(10)
result100 = testfunct(100)

print(result10(9)) #10 is num and 9 is x
print(result100(9)) #creating 2 variations of the same function

result10 = lambda x: x*10
result100 = lambda x: x*100  #this is the same thing as above

numbers_list = [2,6,8,10,11,4,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: num > 7, numbers_list)) #filter expects a function as the first argumenta and an iterable as the second argument

print(filtered_list)

#Map

def addition(n):
    return n + n

numbers = [1,2,3,4]
result = map(addition, numbers)

print(list(result))

#one line result
result = list(map(lambda num: num + num, numbers))
print(result)

numbers = (1,2,3,4)
numbers2 = (5,6,7,8)

result = list(map(lambda x,y: x + y, numbers, numbers2)) #adds the two lists together

print(result)

#zipping
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = [1.5,3.1,5.7]

for item in zip(list1,list2,list3):
    l1,l2,l3 = item
    print(l1)
    print(l2)
    print(l3)