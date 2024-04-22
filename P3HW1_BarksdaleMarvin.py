# Marvin Barksdale
# P3HW1
# 4/21/2024
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1:"))
mod_2 = float(input("Enter grade for Module 2:"))
mod_3 = float(input("Enter grade for Module 3:"))
mod_4 = float(input("Enter grade for Module 4:"))
mod_5 = float(input("Enter grade for Module 5:"))
mod_6 = float(input("Enter grade for Module 6:"))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

# place divider results line

print("------------------------Results----------------------")
print(f"Lowest Grade: {min(grades):.1f}")
print(f"Higest Grade: {max(grades):.1f}")
print(f"Sum of Grades: {sum(grades):.1f}")
print(f"Average: {sum(grades)/len(grades):.2f}")

# place divider lines

print("-----------------------------------------------------")

#add variable for Average

Average = (sum(grades)/len(grades))

# determine letter grade for average


if Average >= 90:
    print('Your grade is: A')
else:
    print()
    
if int(Average) in range(80, 89):
    print('Your grade is: B')

else:
    print()

if int(Average) in range (70,79):
    print('Your grade is: C')

else:
    print()

if int(Average) in range (60, 69):
    print('Your grade is: D')

else:
    print()



if Average <= 59:
    print('Your grade is: F')

else:
    print()


# Thanks I like debugging


