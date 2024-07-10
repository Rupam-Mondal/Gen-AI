import numpy as np

def func(i , j):
    return i * j

arr1 = np.fromfunction(func , (3 , 5) , dtype=int)
print(arr1)

print(arr1.shape)
print(arr1.size)

arr2 = [i for i in range(0 , 5)]
print(arr2)

l = (i for i in range(5))
print(l)

arr3 = np.fromiter(l , float)
print(arr3)

arr4 = np.fromstring("23 24 25" , sep=" " , dtype=int)
print(arr4)

l = list(range(5))

arr5 = np.arange(1 , 10 , 0.1)
print(arr5)

arr6 = np.linspace(1 , 5 , 20)
print(arr6)