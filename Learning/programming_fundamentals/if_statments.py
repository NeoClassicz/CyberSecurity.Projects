import os
os.system('cls')

favorite_number = 7
answer = input("Do you like cheese? (yes/no): ").lower() #lower() converts input to lowercase so NO would be the same as no
if answer == "yes":
    print("My favorite number is", favorite_number)
    if favorite_number > 5:
        print("Woah, That's a big number!")
else:
    if answer == "no":
        print("Apparently you don't like cheese?")
    else:
        print("invalid input, please enter yes or no.")
print("\n") 

hey = input("do you like girls? (yes/no):").lower()
if hey == "yes":
    print("I am glad that you're not gay!")
else:
    if hey == "no":
        print("So you're a fag... werido :/")
    else:
        print("please put in a valid answer")
