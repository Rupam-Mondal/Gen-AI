#iterable>>
#An iterable is any python object/sequential structure/data 
# structure that is capable of returning
#its members one at a time
#permitting it to be iterated over in a for loop
#example>> list, tuples

lis = [1, 2, "Ajay"] #list is an iterable object
for i in lis:
    print(i)

#iteration>>
#iteration is a process of looping through the elements 
# fof an iterable (list, string).
#using a loop
#The process of returning element one by one iteration


for i in "Rupam":
    print(i)

#iterator>> an iterator is an object representing a stream 
#of data>>return the data one by one

#Analogy
#potato(iterable) >> it can not be cooked in original form
#chop/wash the potato >> ready for cooking>>iterator
#the process of cooking>>iteration

#python>> can I prepare s for iteration

s = "Rupam"
a = iter(s) #iterator object>> ready to be iterated
print(a)

print(next(a))

for i in "pwskills": #first conveting the iterable string to iterator object(using iter) and then access using next
    print(i)

t = iter((1, 2, 3, 4))
t = iter({1, 2, 3, 4})
d = iter({"name":"Ajay"})

#generator function
#regular function>> takes a list and gives square of each of the list
def square_number(n):
    result = []
    for i in n:
        result.append(i ** 2)
    return result
print(square_number([5, 10, 15]))

#regular function calculates the square of the values and 
# return in one go since its returning in one go>>memory 
#usage will be more and it will a lot of execution time 
#if there is lot of computation as all the computations 
# will be done first and then the calculation will be 
# returned in one go


#can we have something to generate result one by one one 
#instead of one go yield >> general function uses return 
#statment but a generator function use yield statement

def square_number_generators(n):
    for i in range(n):
        yield i**2

gen = square_number_generators(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))