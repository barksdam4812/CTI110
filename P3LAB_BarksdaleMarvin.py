#Marvin Barksale
#P3LAB
#4/21/2024
#test knowledge of how to write code that uses if/else statements




#Get value from user
change = float(input("Enter an amout of money: $"))

print(f"Change Amount: {change}")
#conterting the value to an integer
change = round(change * 100)

print(f"Change Amount: {change}")

#determine how many coins are needed

num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change


# print if / else statements
# ensure to use singular form if needed
# display plural form of the coins name if needed
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")


if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")


if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")



if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")





              
