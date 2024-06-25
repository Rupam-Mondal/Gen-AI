#numpy >> numerical python
"""
NumPy, short for Numerical Python, is a fundamental 
package for scientific computing in Python. It provides 
support for arrays, matrices, and a variety of mathematical 
functions to operate on these data structures
"""

import numpy as np # type: ignore
print(np.__version__)
# print(np.__doc__)

l1 = [1 , 2 , 3 , "Rupam" , 1.2] #Stores heterogenous data
print(type(l1))

#Numpy stored the data in a numpy array
#It stores homogenous data

""" Numpy computation is very fast because it uses
    c laguage internally since it stores only homogenous data, 
    numpy array is faster
"""

l = [1 , 2 , 3 , 4 , 5]

arr = np.array(l)
print(arr)
print(type(arr))

l.append("Rupam")
arr1 = np.array(l)
print(arr1) #all will be converted into string

print(arr.ndim) #It will give number of dimention present in
#an array

arr2 = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
print(arr2)
print(arr2.ndim)

mat = np.matrix([1 , 2 , 3 , 4])
print(mat)
print(type(mat))

arr3 = np.array([[[1 , 2] , [4 , 5]]])
print(arr3)
print(type(arr3))

#asanyarray will covert the input to the array , but passing array
#will not do anything

print(np.asanyarray([1 , 2 , 3]))
print(np.asanyarray(arr1))

tu = ([1 , 2 , 3] ,[4 , 5 , 6])
print(np.array(tu))

# accesing element of array
print(arr[0])
#Array is mutable
arr[0] = 1000
print(arr)

a = arr #Both are pointing to same mem location changing any of them
#will reflect to both also known as shallow copy

b = arr.copy() # This is known as deep copy
print(b)
b[0] = 5000
print(b)


#Multiple approach to generate array

print(np.fromfunction(lambda i , j: i==j , (3 , 3))) #Construct an array by 
#executing a function over each coordinate

print(np.fromfunction(lambda i , j: i * j , (3 , 3))) 

print(arr1.size)
print(arr1.shape)

iterator = (i for i in range(5))

print(np.fromiter(iterator , int))
print(np.fromstring('22 23 24' , sep=" " , dtype=int))

s = "Rupam , ajay , sanjay"
print(np.array(s.split(",")))

#Other method to generate to sequence of number
l = list(range(0 , 10)) # Normal python
print(l)

print(np.arange(1 , 10)) # No need to write list here it directly
#returns a sequence in given range