#lambda function>> anonymous function
#syntax 
#lambda arguments : expression >> no need of return 
#statement and def keyword

def square(x):
    return x**2

print(square(2))

a = lambda x: x ** 2
print(a(2))

add = lambda a, b: a+b
print(add(2 , 3))

is_even = lambda x: x%2 == 0
print(is_even(4))

fib = lambda n: n if n<=1 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(10)])

fact_num = lambda n: 1 if n==0 else n*fact_num(n-1)
print(fact_num(5))

#map >> executes a specified function for each of iterm 
# of an iterable
#syntax >> map(func,*iterables)

l = [1, 2, 3, 4, 5]
def square(l):
    sq = []
    for i in l:
        sq.append(i**2)
    return sq

def sq(x):
    return x**2 

#map(func, iterable)
sq_list = list(map(sq, l))
print(sq_list)

#reduce >> folding/reduction
#syntax>> #reduce(func, iterable)
#reduce will always take two arguement function
from functools import reduce