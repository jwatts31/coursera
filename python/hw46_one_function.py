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
def computepay(hours_worked,pay_rate):
    
    try:
        float_hours_worked = float(hours_worked) 
    except:
        print "Numeric Value was not entered for the hours worked, please enter numeric value"
        quit()
    try:
        float_pay_rate = float(pay_rate)
    except:
        print "Numeric Value was not entered for the pay rate, please enter numeric value"
        quit() 
    
    if float_hours_worked <= 40:
        totalPay = float("{0:.2f}".format(float_hours_worked * float_pay_rate))
    elif float_hours_worked > 40:
    
        overtimeRate = 1.5
        overtimeTotalRate = float_pay_rate * overtimeRate
        overTimeBegins = 40
    
        #calculate non overtime pay
        initialPay = overTimeBegins * float_pay_rate
        
        #calculate overtime pay
        totalOvertime = float_hours_worked - overTimeBegins
        overTimePay =  totalOvertime * overtimeTotalRate
        totalPay = float("{0:.2f}".format(overTimePay + initialPay))
    
    else:
        print "Could not calculate the total pay"
    
    return totalPay