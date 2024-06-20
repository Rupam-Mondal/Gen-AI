count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop ended normally")

#With break statement
count = 0
while count < 10:
    print(count)
    if count == 5:
        break
    count += 1

#With continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
