'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

def get_Senders(file_name):
    
    try:
        file_handler = open(file_name,'r')
    except:
        print "The filename you have entered is invalid"
        quit()
    
    #Initialize dict
    emails = {}
    
    for line in file_handler:
        #Strip white spaces on the right of the line
        line = line.rstrip()
        #Check to see if the line starts with 'From: ' as specified in the instructions
        if line.startswith('From '):
            line_spl = line.split()
            
            for word in line_spl:
                #Find which item in the list has an @
                    if '@' in word:
                        #If the words exists add 1 to the count
                        #If the word does not exist, initalize to 0 and add 1
                        emails[word] = emails.get(word,0)+1   
        else:
            continue
    
    return emails
        

#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
emails = get_Senders(file_name)
#get the most prolific committer
#Coursera auto grader does nto support: maximum = max(emails, key=emails.get), have to do by hand
max_email = None
max_count = None

for email,count in emails.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
    else:
        continue
print max_email,max_count