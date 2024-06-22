#List are ordered collection of items
#[]
#list is like a shopping bag which can store everything
#cab store any datatype


grocery_list = ["Milk", "Orange", 1, 2.2, True, 3+5j]
print(type(grocery_list))

#lists are mutable
print(grocery_list[1:4])

lis = ["Apple", "Orange"]
lis.append("Mango")
print(lis)

#use cases
playlist = []
playlist.append("sare jahan se acha")
playlist.append("Ae mere watan ke logo")
playlist.append("Tughe dekha toh")

#Insert
lis.insert(1, "potato") # Insert object before index.
print(lis)


my_list = ["Apple", "Banana", "orange"]
brothers_list = ["brinjal", "potato"]
my_list.extend(brothers_list) #will extend the first list

print(list(range(0 , 10)))
print("Milk" in grocery_list)

#deep copy and shallow copy

#shallow copy >> value will change with change in other list

a = grocery_list #shallow copy both pointing same memory location