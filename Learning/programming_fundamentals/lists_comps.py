import os
os.system('cls')

numbers = [1, 2, 3, 4, 5, 6]
# other = []
print(numbers)
# print(other)

# add three to each number.
# for number in numbers:
#     other.append(number + 3) 

other = [number + 3 for number in numbers]
print(numbers)
print(other)