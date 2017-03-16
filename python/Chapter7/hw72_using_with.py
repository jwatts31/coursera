'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at 
http://www.pythonlearn.com/code/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
'''

def calculateSum(file_name):
    
    with open(file_name,'r') as file_handler:
   
        #Initialize count & average
        average = []
        for line in file_handler:
            line = line.rstrip()
            #Does the line start with X-DSPAM-Confidence:?
            if line.startswith('X-DSPAM-Confidence:'):
                    #Find the position of the colon
                    post_semi_colon = line.find(':')
                    #Get all characters after the colon
                    value = line[post_semi_colon+1:]
                    #Strip the white space and covert to a float
                    float_value = float(value.strip())
                    #Append it to the list
                    average.append(float_value)
        
        #I could do this in the above for loop but breaking it out in case I ever want to
        #use that data again
        add_value = 0
        for value in average:
            add_value = add_value + value
        
        #Calculate the average
        if len(average) >0:
            calc_average = (add_value)/len(average)
        else:
            calc_average = 0
        
        return calc_average
    
'''   
#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
average = calculateSum(file_name)

print "Average spam confidence:",average
'''              
                
    