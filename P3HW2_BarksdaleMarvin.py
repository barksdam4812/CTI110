# Marvin Barksdale
# P3HW2
# 4/21/2024
# Assignment assess understanding of decision structures

#enter variables
name = input("Enter employee's name:")
hours = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee's pay rate:"))
overtime = (hours - 40)
overtime_pay = (overtime * 1.5)
regular_pay = (pay_rate * 40)
gross = (hours * pay_rate)
#print divider
print("--------------------------------------------")
print("Employee name:", name)
print()

print("Hours Worked        Pay Rate        OverTime        OverTime Pay        RegHour Pay        Gross Pay")

#add in hours
print("-------------------------------------------------------------------------------------------------------")
#Dead code that did not work
#print(hours)
#print(f'{pay_rate:<55}')
#print(hours * pay_rate)
print(f'{hours:<20.2f} {pay_rate:<10.2f}     {overtime:<10.2f}       {overtime_pay:<10.2f}          {regular_pay:<10.2f}         {gross:<10.2f}')


#this was fun to try and put together!
