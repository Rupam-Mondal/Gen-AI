import numpy as np

print(np.__version__)

lis = [1 , 2 , 3 , "Rupam" , 2.3]
print(type(lis))

l = [1 , 2 , 3 , 4]
print(type(l))

arr = np.array(l)
print(type(arr))
print(type(l))

print(arr.ndim)

arr1 = np.array([[1 , 2 , 3] , [2 , 4 , 5]])
print(arr1.ndim)

arr2 = np.matrix(l)
print(arr2)
print(arr2.ndim)

arr3 = np.array([[[1 , 2]]])
print(arr3)

np.asarray(l)
np.array(arr1)
np.asanyarray(arr1)

t = ([1 , 2 , 3] , [4 , 5 , 6])
mat = np.matrix(t)
print(mat)

print(arr1[0][0])


#Shallow copy
a = arr
print(a)
a[0] = 0
print(arr)

#Deep copy
b = arr.copy()