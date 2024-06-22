#dictionary is a data structure that stores 
# data as key value pair
#Keys are unique and immutable

#Note:dictionaries are unordered. but from Python 3.7 version, 
# dictionaries retain the order of insertion. 
#This means that if you iterate over a dictionary, the items will be returned in the order they were added.

s = {}
print(type(s))

d = {"name":"Ajay", "email":"aj@gmail.com", "contact": 1234}
print(d["email"])
d = {'name': ['Sanjay', 'Ajay', 1, 2],
    'email': 'aj@gmail.com',
    'contact': (1234, 678)}


print(d['name'][1])

restaurant_menu = {
    'Dish1': {'name': 'Pasta Carbonara', 'price': 15.99, 'description': 'Creamy pasta with bacon and parmesan'},
    'Dish2': {'name': 'Chicken Caesar Salad', 'price': 12.50, 'description': 'Grilled chicken with romaine lettuce and Caesar dressing'},
    'Dish3': {'name': 'Margherita Pizza', 'price': 14.00, 'description': 'Pizza topped with tomato, mozzarella, and basil'}
}

print(restaurant_menu.keys())
print(restaurant_menu.values())
print(restaurant_menu.items())