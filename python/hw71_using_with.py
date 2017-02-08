'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
'''

def printUpper(file_name):
    
    with open(file_name,'r') as file:
        for line in file:
            line = line.rstrip()
            print line.upper()

        
#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
printUpper(file_name)


       
