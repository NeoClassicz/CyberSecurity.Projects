import os
os.system('cls')

class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

user_1 = Person( age=60,
               weight=200,
               height=75,
               first_name="bob", 
               last_name="fart",
)

instanced_dict = vars(user_1)

print(instanced_dict)