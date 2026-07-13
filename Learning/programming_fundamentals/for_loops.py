import os
os.system('cls')

numbers = [1, 2, 3, 4, 5]
words = ['the', 'cheese', 'is', 'good']
user = ('Breandan', 'King', 19, 'pizza')
foods = dict(pizza=True, onions=False, olives=False, salami=True)

# print(numbers)
# print(words)
# print(user)
# print(foods)

# The standard for loop in python
# for element in words:
#     print(element)

# for index in range(1, len(numbers)): #range(start, stop, step)
#     element = numbers[index]
#     print(element)

# for loops and dictionaries
for key, value in foods.items():
    print(key, value )