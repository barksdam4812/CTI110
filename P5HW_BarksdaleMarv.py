#Marvin Barksdale
# 5/4/2024
#P5HW1
#use of loops, functions, and module import


#import rancom - this is needed to pull random number below

import random

#set up main function

def main_one():
    print("Welcome to Math Quiz")
    print()
    print()
    print("MAIN MENU")
    print('------------------------------------')
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

main_one()   

selection = int(input("Please choose one of the menu options: "))

#if selection == 1:

    

#random number generator to be used. make sure to generate two different number

#section will be designed to handle the addition once selection is made

while selection == 1:

    number_1 = random.randint(1, 100)
    print(" ", number_1)

    number_2 = random.randint(1, 100)
    print("+", number_2)
    print()
    user_answer = int(input("Enter answer.\n" ))
    Add = number_1 + number_2


    if user_answer == Add:
        print("Congratulations!!!! Your answer is correct.")
        

    if user_answer > Add:
        print(f"Try again: {user_answer}")
        print("Sorry your guess is too high)")
        

    if user_answer < Add:
        print(f"Try again:{user_answer} ")
        print("Sorry your guess is too low")       
              

#section two will be designed to handle the subtraction  once randon numbers is generated

while selection == 2:
    number_1 = random.randint(101, 200)
    print(" ", number_1)

    number_2 = random.randint(1, 100)
    print("-", number_2)
    print()
    user_answer = int(input("Enter answer.\n" ))
    Add = number_1 - number_2

    if user_answer == Add:
        print("Congratulations!!!! Your answer is correct.")

    if user_answer > Add:
        print(f"Try again: ")
        print("Sorry your guess is too high)")
    if user_answer < Add:
        print(f"Try again: ")
        print("Sorry your guess is too low")


main_one

#for selection of three closing out what happens 

if selection == 3:
    print("Thank you for playing...")
    print("Bye!!")
else:
    print(f"This selection is not allowed")
    selection = int(input("Please choose one of the menu options: "))

    quit()












   
    


    