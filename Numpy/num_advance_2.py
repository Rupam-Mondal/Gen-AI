import numpy as np

arr1 = np.random.randint(1 , 3 , (3 , 3))
arr2 = np.random.randint(1 , 3 , (3 , 3))

print(arr1)
print(arr2)

print(arr1.flatten())

#Expand dimention

arr = np.array([1 , 2 , 3 , 4])
print(np.expand_dims(arr , axis = 0)) #0 means x axis and 1 means y axis
print(np.expand_dims(arr , axis = 1))

#Squeezing the dimension bu 1 dimension
np.squeeze(arr)

#Repeating

print(np.repeat(arr1 , 2 , axis = 1))