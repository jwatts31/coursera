'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
'''

def findEmailsFrom(file_name):

    with open(file_name,'r') as file_handler:
        
        #Initialize list    
        emails = []
        for line in file_handler:
            #Strip white spaces on the right of the line
            line = line.rstrip()
            #Catch the case where the line starts with From: 
            if line.startswith('From:'):
                continue
            elif line.startswith('From'):
                line_spl = line.split()
                for word in line_spl:
                    #Find which item in the list has an @
                    if '@' in word:
                        emails.append(word) 
                    else:
                        continue  
            else:
                continue
    
        return emails

'''    
#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
emails = findEmailsFrom(file_name)

for email in emails:
    print email

print "There were",len(emails),"lines in the file with From as the first word"
'''