#set variables
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