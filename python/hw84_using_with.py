'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

def sortWordsInFile(file_name):
    
    with open(file_name,'r') as file_handler:
    
        #Initialize list
        words_in_txt= []
        for line in file_handler:
            #Strip white spaces on the right of the line
            line = line.rstrip()
            #Split on white spaces
            line_spl = line.split()
            
            #Loop through each word in the list, if it is no in the list words_in_txt, add it to the list
            for word in line_spl:
                if word not in words_in_txt:
                    words_in_txt.append(word)
                else:
                    continue
        
        #Sort the list
        words_in_txt.sort()
        
        return words_in_txt

'''
#This is for the class
file_name = raw_input("Enter in valid filename: ")

#Calling Function
sorted_words = sortWords(file_name)

print sorted_words
'''