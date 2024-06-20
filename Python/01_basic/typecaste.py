"""
Typecaste is a method to convert any datatype to
otherdatatype
"""
#Explicite typecasting
a = int("2") + 2
print(a)

b = bool(1)
print(b)

"""
Implicit Type Casting (Coercion)


Implicit type casting occurs when Python 
automatically converts one data type to another 
without the programmer's intervention. This is 
usually done to avoid data loss in 
expressions where different data types are mixed.
"""

# Implicit type casting in Python
integer_value = 10
float_value = 5.5

# Adding an integer and a float
result = integer_value + float_value

print(result)       # Output: 15.5
print(type(result)) # Output: <class 'float'>
