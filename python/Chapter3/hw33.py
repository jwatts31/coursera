'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
    Score Grade
    >= 0.9 A
    >= 0.8 B
    >= 0.7 C
    >= 0.6 D
    < 0.6 F
    If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''

score = raw_input("Enter a score betweem 0.0 and 1.0:")

try:
    floatScore = float(score)
except:
    print "Numeric Value was not entered, please enter numeric value"
    quit()

if (0.9 <= floatScore <= 1.0):
    print "A"
elif (.80 <= floatScore <= .89):
    print "B"
elif (.70 <= floatScore <= .79):
    print "C"
elif (0.6 <= floatScore <= .69):
    print "D"
elif (0.0 <= floatScore < 0.6):
    print "F"
else:
    print "Score Range must be between 0.0 to 1.0"
