s = "Rupam"
print(type(s))
print("string" + ">>" +"concatenation")

string1 = "I  am a good student"
print(string1[0:4]) #4 is exclusive [a, b]>>it will give 
#result till b-1 index

print(string1[0:])
#start_index:end_index>> if you not provide end idex, 
# it will be default give 
#substring till the last index


strings2 = "pwskills"
#except the last three character
print(strings2[:-3])

#you want only last characters
print(strings2[-3:])

string2 = "hello world!"
#Last argument is actually number 
# of jump in every iteration
string2[0:5:1] #by default step is 1 

s = "I am a student"
print(len(s))

print(s.replace("student", "teacher"))

text = "Hello World"
print(text.lower())
print(text.upper())
text = " Iam a Student"
print(text.swapcase())

#string searching
sentence = "I am a student at pwskills"
print("am" in sentence)


email = "ajay123@gmail.com"
if "@" in email:
    print("valid email")
else:
    print("Invalid email")