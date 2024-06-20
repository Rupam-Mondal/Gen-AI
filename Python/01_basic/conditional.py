#Type 1

x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif 0 < x < 10:
    print("x is positive but less than 10")
else:
    print("x is 10 or more")

#Type 2

x = 5
result = "x is positive" if x > 0 else "x is zero or negative"
print(result)  # Output: x is positive
