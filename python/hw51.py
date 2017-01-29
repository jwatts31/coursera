'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
'''

#initialize variables
maxNum = None
minNum = None
numsEnter = None
numList = []


while True:
    numsEnter = raw_input("Enter a number: ")
    if numsEnter == "done":
        break
    try:
        intNumsEnter = int(numsEnter)
    except:
        print "Invalid input"
        continue
    
    numList.append(intNumsEnter)

print "Maximum is",max(numList)
print "Minimum is",min(numList)