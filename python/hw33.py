#What is my grade
score = raw_input("Enter in the score:")
try:
    floatScore = float(score)
except:
    print "Numeric Value was not entered, please enter numeric value"
    quit()

if (floatScore >= 0.9) and (floatScore <= 1.0):
    print "A"
elif (floatScore >= 0.8) and (floatScore <= .89):
    print "B"
elif (floatScore >= 0.7) and (floatScore <= .79):
    print "C"
elif (floatScore >= 0.6) and (floatScore <= .69):
    print "D"
elif (floatScore < 0.6) and (floatScore >= 0.0):
    print "F"
else:
    print "Score Range must be between 0.0 to 1.0"