'''
4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function.
'''


#def computepay
def computepay(floatHoursWorked,floatPayRate):
    if floatHoursWorked <= 40:
        totalPay = floatHoursWorked * floatPayRate
    elif floatHoursWorked > 40:
    
        overtimeRate = 1.5
        overtimeTotalRate = floatPayRate * overtimeRate
        overTimeBegins = 40
    
        #calculate non overtime pay
        initialPay = overTimeBegins * floatPayRate
        
        #calculate overtime pay
        totalOvertime = floatHoursWorked - overTimeBegins
        overTimePay =  totalOvertime * overtimeTotalRate
        totalPay = overTimePay + initialPay
    
    else:
        print "Could not calculate the total pay"
    
    return totalPay
    

hoursWorked = raw_input("Enter in hours worked:")

try:
    floatHoursWorked = float(hoursWorked) 
except:
    print "Numeric Value was not entered for the hours worked, please enter numeric value"
    quit()

payRate = raw_input("What is the pay rate for this employee:")

try:
    floatPayRate = float(payRate)
except:
    print "Numeric Value was not entered for the pay rate, please enter numeric value"
    quit()

totalPay = computepay(floatHoursWorked,floatPayRate)
print totalPay
