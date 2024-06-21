#List(mutable)
list = [1 , 2 , 3 , 4 , 5]
print(type(list))
list1 = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]]

#Tuple(Immutable)
tu = (1 , 2 , 3 , 4)
tu1 = ((1 , 2) , (3 , 4) , (5 , 6))
print(type(tu))
print(tu[1])
print(tu[-1])

#Sets(Mutable and unique)
#No concept of indexing
s = {'a' , 'a' , 'a' , 1}
print(s) #Not follows the user given order

#Dictionary
phonebook = {"Dad" : 1234 , "Mom" : 1235}
print(phonebook["Dad"])