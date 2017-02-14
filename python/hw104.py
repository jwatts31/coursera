'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

def get_hours(file_name):
    try:
        file_handler = open(file_name,'r')
    except:
        print "The filename you have entered is invalid"
        quit()
    
    time_and_count = {}
    
    for line in file_handler:
        line = line.rstrip()
        
        if line.startswith('From '):
            #Strip white spaces on the right of the line
            line_spl = line.split()
            #Would use a regular expression here but since it has not been covered yet, I will not use it
            for word in line_spl:
                #Find which item in the list has a :
                if ':' in word:
                    #Split on the colon to get the hour
                    hour_spl = word.split(':')
                    If the words exists add 1 to the count
                    #If the hour does not exist, initalize to 0 and add 1
                    #If it does exist, add one
                    time_and_count[hour_spl[0]] = time_and_count.get(hour_spl[0], 0) + 1
                else:
                    continue
        else:
            continue

    return time_and_count
            
#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
time_count = get_hours(file_name)

sorted_time_count = sorted([ (k,v) for k,v in time_count.items()])

for k,v in sorted_time_count:
    print k,v