#math library contains collection of function
import math as m

print(m.ceil(6.5))

print(m.floor(6.5))

#user defined function
def func():
    #body of fucntion
    return 6 , 5


def greetings(): 
    print("Welcome to the office")

greetings()

def greetings(name): #passing a variable inside a function >> name is positional arguement
    print("Welcome to the office", name)

greetings("Rupam")

def func():
    print("This is my first function")
    
func()
print(type(func()))

def func():#return>> output of a function
    #do something
    return "This is my first function"

print(func() + " in Python")

def func():
    return "this is my first function", 1, 2.2, True, 3+7j

a , b , c , d , e = func()
print(a)
print(b)
print(c)
print(d)
print(e)

def square_no(a): #a is called as an arguement
    return a*a

print(square_no(5))

#default argement
def sum1(b, c, a=0):
    return a+b+c

print(sum1(4 , 5))
print(sum1(4 , 5 , 3))

def sum1(b=5, c=0, a=0):
    return a+b+c
print(sum1(a=3))