import os
os.system('cls') 

# If you highlight multiple lines of code or just one and do ctrl + / it will comment those lines out.

ingredients = [
    'cheese',
    'pepperoni', 
    'mushrooms', 
    'onions'
]
numbers = [7, 2, 3, 5, 11]
word = ['c', 'a', 't',]


# print(ingredients)
# print(numbers)
# print(word)

# #
# new_list = ingredients + numbers
# print(new_list)

# Accessing Elements and Slicing
second_ingredient = ingredients[2]
#print(second_ingredient)
number_of_ingredients = len(ingredients)
#print(number_of_ingredients)

# Change the element
# ingredients[3]= 'more cheese'
# del ingredients[3]
# print(ingredients)
#john_ingredients = ingredients[0:4:2] #slicing the list to start at the first element, stop at the fourth element, and then only print every second element. Start, stop step, 
justin_ingredients = ingredients[:]
justin_ingredients[1:2] = ['extra cheese']
#print(justin_ingredients)

# list of strings to string?
#string_word = ''.join(word)
#rint(string_word)
#back_to_list = list(string_word) 
#print(back_to_list)

letters1 = ['a', 'b', 'c' ,'d']
numbers1 = [1, 2, 3, 4]

numbers_and_letters = letters1 + numbers1
stringword = ''.join(letters1)
#print(stringword) 

letters2 = ['c', 'a', 't',]
letters2.append('dick') #.append() adds that string to the end of the list.
print(dir(letters2))
print(letters2)

letters2.pop() #.pop() takes the last string off the end of the list.
print(letters2)
