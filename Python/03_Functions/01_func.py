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


def only_numeric(a):
    n = []
    for i in a:
        if type(i) == int or type(i) == float:
            n.append(i)
    return n

only_numeric([1, 2.2, "Ajay", True, 3+7j, "pwskills", 5, 6])

#A function which can take any no of values and return the sum

def sum1(*args):
    s = 0
    for i in args:
        s = s+i
    return s

print(sum1(1, 2, 100))


def return_list(*args):
    l = []
    for i in args:
        if type(i) == list:
            l.append(i)
    return l

print(return_list(1, 2, 2.3, 5+7j, {2,3},[4, 5, [6, 7]], [1, 2, 3, 4], (2,3), True, "Ajay"))

def marks_in_subject(**kwargs):
    def total_marks(marks_list):
        return sum(marks_list)
    marks_list = []
    for sub, marks in kwargs.items():
        marks_list.append(marks)
        
    return total_marks(marks_list)