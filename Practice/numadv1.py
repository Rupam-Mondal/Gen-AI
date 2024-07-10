import numpy as np

a = np.zeros(5 , dtype=int)
print(a)

b = np.zeros((3 , 5))
print(b)

c = np.ones(4 , dtype=int)
print(c)

d = np.zeros((3 , 3 , 4) , dtype=int)
print(d)    

e = np.zeros((3 , 3 , 3 , 4) , dtype=int)
print(e)

print(b - 1)

f = np.eye(4 , dtype=int)
print(f)

g = np.empty(5 , dtype=int)
print(g)