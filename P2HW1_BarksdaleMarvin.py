# Marvin Barksdale
# 4/4/2024
# P2HW1
# Assess student ability to edit and enhance existing programs



print("This program calculates and displays travel expenses")
print()
Budget = int(input("Enter Budget:"))
print()
Location = input("Enter your travel destination:")
print()
Fuel = int(input("How much do you think you will spend on gas?"))
print()
Accomodation = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
Food = int(input("Last, how much do  you need for food?"))
print("----------------------Travel Expenses-------------------")
print("location:", Location)
print(f"Initial Budget ${Budget:.2f}")
print(f"Fuel ${Fuel:.2f}")
print(f"Accomodation ${Accomodation:.2f}")
print(f"Food ${Food:.2f}")
print("--------------------------------------------------------")
print()
print(f"Remaining Balance ${Budget-Fuel-Accomodation-Food:.2f}")
print()
print()
print()

print('## ##### ######     ###    ##   ##  #######  ####     ')
print('## ## ##  ##  ##   ## ##   ##   ##   ##   #   ##      ')
print('   ##     ##  ##  ##   ##  ##   ##   ##       ##      ')
print('   ##     #####   ##   ##   ## ##    ####     ##      ')
print('   ##     ## ##   #######   ## ##    ##       ##      ')
print('   ##     ## ##   ##   ##    ###     ##   #   ##  ##  ')
print('  ####   #### ##  ##   ##    ###    #######  #######')


#I am not too sure about providing Pseudocode but i will give it a try

#inform user of the purpose of program(opening line)
#use line spacing for a cleaner look
#prompt user to input budget information
#   display budget information
#prompt user to input destination information
#   display destination information
#pronpt user to input estimatated fuel cost
#   display fuel cost infromation to user
#prontp user for accomodation estimation
#   display accomodation 
#prompt user to input food estimation
#   display food estimation on second line
#display divider text with verbage Travel expenses. this divides input from output
#display results
#utilize correct spacing between sections
#Budget-Fuel-Accomodation-Food out put to remaining balance
#display remaining balance on the final screen
#attempt to write out pseudocode information.
#place Travel ASCII at the bottom