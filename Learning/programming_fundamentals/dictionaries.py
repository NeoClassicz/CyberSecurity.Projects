import os
os.system('cls')


user = { 
    'first_name': 'Breandan', 
    'last_name': 'King', 
    'age': 19 
}
data = [
    ('first_name', 'Breandan'),
    ('last_name', 'King'),
    ('age', 19)
]
user = dict(data)
# user = dict(first_name='Breandan', last_name='King', age=19)

foods = { 0: 'pizza', 1: 'cookie' }


# Getting element (values)
first_name = user['first_name']
print(first_name)
f = foods[0]
print(f)

# set a value
user['age']
print(user)

print(user.values()) #you can do user.keys(), user.values() user.items().

print(user.get('last_name'))
