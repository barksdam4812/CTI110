#Marvin Barksdale
#Date - 4/14/2024
#P2HW2
# Assignment assess student understanding of lits



#get module information from user

#make sure to use float instead of int

Module_1 = float(input("Enter grade for Module 1:"))
Module_2 = float(input("Enter grade for Module 2:"))
Module_3 = float(input("Enter grade for Module 3:"))
Module_4 = float(input("Enter grade for Module 4:"))
Module_5 = float(input("Enter grade for Module 5:"))
Module_6 = float(input("Enter grade for Module 6:"))

#create list containing user input informaiton

Module_score = [Module_1, Module_2, Module_3, Module_4,Module_5,Module_6]

#create results spacer
print('---------------------Results-------------------------')

# display results using f string
# ensure results show only two decimal positions only
# Average needs to show two decimal positions with tie in.
print(f"Lowest Grade: {min(Module_score):.2f}")
print(f"Higest Grade: {max(Module_score):.2f}")
print(f"Sum of Grades: {sum(Module_score):.2f}")
print(f"Average: {sum(Module_score)/len(Module_score):.2f}")

print('-----------------------------------------------------')

# this was challenging I am learning a lot. Thanks!
