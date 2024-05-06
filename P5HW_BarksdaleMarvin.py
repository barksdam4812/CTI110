#Marvin Barksdale
# 5/4/2024
#P5HW1
#use of loops, functions, and module import


#place import randome code
# this is needed to pull random numbers later in code



def entire():
    import random

    #create main function

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

    #place import and generate random numbers
    # two numbers will be needed

    number_1 = random.randint(101, 200)

    number_2 = random.randint(1, 100)

    # create function to handle the addition

    def Addition_num():
        print(" ", number_1)
        print("+", number_2)
    Addition_num

    # create function to handle subtraction
    def Subtraction_num():
        print(" ", number_1)
        print("-", number_2)
    Subtraction_num

    #create comment functions to be called
    def Quit_num():
        print("Thank you for playing...")
        print("Bye!!!")
        quit
    Quit_num

    def wrong_num():
        print("This is not a valid selection")
        selection = int(input("Please choose one of the menu options: "))
    wrong_num

    def addition_comments():
        if user_answer == add:
            print("Congratulations!!!! Your answer is correct.")
            print()
            entire()

        if user_answer > add:
            print(f"Try again: {user_answer}")
            print("Sorry your guess is too high)")
                
        if user_answer < add:
            print(f"Try again:{user_answer} ")
            print("Sorry your guess is too low")
    addition_comments


    def subtraction_comments():
        if user_answer == subtract:
            print("Congratulations!!!! Your answer is correct.")
            print()
            entire()

        if user_answer > subtract:
            print(f"Try again: {user_answer}")
            print("Sorry your guess is too high)")

        if user_answer < subtract:
            print(f"Try again:{user_answer} ")
            print("Sorry your guess is too low")
    subtraction_comments

    #place functions higher in code so it is identified and pythin can pull


    #addition and subtraction math

    add = number_1 + number_2
    subtract = number_1 - number_2

    if selection == 1: Addition_num()
    if selection == 2: Subtraction_num()
    if selection == 3: Quit_num()
    if selection > 3: wrong_num()
    if selection <=0: wrong_num()

    #user input needed

    user_answer = int(input("Enter answer.\n" ))




    if selection == 1: addition_comments()
    if selection == 2: subtraction_comments()







    #subtract
entire()