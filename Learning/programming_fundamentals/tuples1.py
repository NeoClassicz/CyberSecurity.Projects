import os
os.system('cls')

# define some tuples

user_fieldnames = ('first name', 'last name', 'age', 'favorite food', 'qualities')
user = ('Breandan', 'King', '19', 'chicken', ['strong', 'athletic'])
numbers = (1, 2, 3, 4, 5, 6)
one_number = (1, )
another_number = (1)
empty = ()

# print(type(one_number))
# print(type(another_number))
# print(type(empty))

# operations with tuples
# result = numbers + user
# result = numbers * 3
# print(result)

#accessing elements
print(user)
first_name = user[0:]
print(first_name)