'''
3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
'''
hoursWorked = raw_input("Enter in hours worked:")
floatHoursWorked = float(hoursWorked) 
payRate = raw_input("What is the pay rate for this employee:")
floatPayRate = float(payRate)


if floatHoursWorked <= 40:
    totalPay = floatHoursWorked * floatPayRate
elif floatHoursWorked > 40:
    #Set overtime rate and total hours when overtime begins 
    overtimeRate = 1.5
    overtimeTotalRate = floatPayRate * overtimeRate
    overTimeBegins = 40
    
    #calculate non overtime pay
    initialPay = overTimeBegins * floatPayRate
    
    #Calculate overtime pay
    totalOvertime = floatHoursWorked - overTimeBegins
    overTimePay =  totalOvertime * overtimeTotalRate
    totalPay = overTimePay + initialPay
else:
    print "Could not determine the number of hours worked"

print totalPay
