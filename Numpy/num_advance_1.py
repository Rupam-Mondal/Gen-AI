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

import random

print(random.choice((1 , 2 , 3 , 4)))

print(random.randrange(1 , 10))

print(random.random())

list = [1 , 2 , 3 , 4]
random.shuffle(list)
print(list)

print(np.random.random_sample((3)))
print(np.random.rand(3 , 3))

#Gives randome dimetion array in given range 1 to 5(exclusive)
b = np.random.randint(1 , 5 , size=(3 , 4))
print(b)
print(b.ndim)
print(b.size)


b1 = b.reshape(2 , 6) #Size should be same as previous
print(b1)

print(b.reshape(2 , 6).base) #Gives the orginal array


print(b.reshape(2 , 2 , 3)) #Again multiple should be same as original size

#Conditions on array

print(b > 3) #In b array which elements satisfy this condition

print(b[b > 1])

print(b[0])
print(b[0][1])

print(b[0:3])

#Matrix multiplication

#If you write arr1 @ arr2 you will get mat multiplication
#also np.dot(arr1 , arr2)