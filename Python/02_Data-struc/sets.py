#Duplicates are not allowed and it is unordered
#Indexing is not valid

s = {}
print(type(s))

s = {1, 2, 1, 2, 2, "Ajay", "Ajay", "Ajay", "ajay", "ajay"}
print(s)

list1 = list(s)
print(type(s))

#Set is mutable
s.add(100)

s.pop() #it is not compulsory that it will remove the last element

s.remove(2) #removes a spcific element
s.update("Ajay")
s.update(["Rupam"])

print(s)



s1 = {"hiking", "reading", "coding"}
s2 = {"coding", "photography", "travelling"}

#union>> combine all the elements
s1 | s2


#intersection >> common elements
s1 & s2

#difference
s1-s2

#frozen sets>>immutable version of set, cannot be added or removed any new element
my_fs = frozenset([1, 2, 2, 2, 3, 3, 4, 5])

print(type(my_fs))