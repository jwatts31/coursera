#calculate overtime pay if neccessary

hoursWorked = raw_input("Enter in hours worked:")
floatHoursWorked = float(hoursWorked) 
payRate = raw_input("What is the pay rate for this employee:")
floatPayRate = float(payRate)


if floatHoursWorked <= 40:
    totalPay = floatHoursWorked * floatPayRate
elif floatHoursWorked > 40:
    
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
    print "Something went wrong"

print totalPay