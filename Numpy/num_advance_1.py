import numpy as np

# An array contains all zero
arr = np.zeros(5)
print(arr)

arr1 = np.zeros(5, dtype=int)
print(arr1)

arr2 = np.zeros((5 , 5), dtype=int)
print(arr2)

# An array contains all one
a = np.ones(5)
print(a)

a1 = np.ones(5, dtype=int)
print(a1)

a2 = np.ones((5 , 5), dtype=int)
print(a2)


#Threedimentional array
aa1 =np.zeros((2 , 3 , 3) , dtype=int) #second row third coloum
print(aa1)

""" You can increase as many dimention you want last two param
    will always be row and coloum
"""

arr = np.zeros((3 , 4) , dtype=int)
print(arr)

print((arr + 1)) # added 1 to all elements
print((arr + 1) * 7)
print(arr - 1)

#np eye--> Return a 2-D array with ones on the diagonal and zeros elsewhere.

print(np.eye(3 , dtype=int))

#np empty -->
print(np.empty((3, 4)))