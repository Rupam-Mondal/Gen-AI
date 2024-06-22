# Tuples are ordered collection of elements

tu = (1 , "Rupam" , 2 , 2.3)
print(type(tu))

print(tu[1])

# Tuples are immutable we can not modify 
# any elements in tuple

empid = (1 , 2 , 3 , 4 , 5)
# When you do not wanna change data of any dataset then
#Tuple is used

tuple1 = ("pwskills" , 1 , 1 , 1)
print(tuple1.count(1))

#slice
print(tuple1[0:2])
#for reverse
print(tuple1[::-1])

#min and max
t1 = (1 , 2)
print(min(t1))
print(max(t1))


#merge two tuple
t2 = (3 , 4)
t3 = (t1 , t2)
print(t3)

#length
print(len(t1))

#Membership operators are also present
#combine
print(t1 + t2)