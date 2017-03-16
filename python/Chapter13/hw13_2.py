'''
Welcome Justin W from Using Python to Access Web Data

Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_350839.json (Sum ends with 23)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python solution.py 
Enter location: http://python-data.dr-chuck.net/comments_42.json
Retrieving http://python-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''

import urllib 
import json

#address = 'http://python-data.dr-chuck.net/comments_42.json'

def parse_comment_counts(address):
    
    #Initialize variable
    comments = []
    
    #Check the address
    if len(address) < 1:
        print "URL is invalid, please enter a valid URL"
        return None
    else:
        try:
            url = urllib.urlopen(address)
        except:
            print "Unable to open address"
            return None
        
        data = url.read() 
        
        #Attempt to load JSON
        try: 
            js = json.loads(data)  
        except: 
            js = None
        
        #If set to None, exit
        if js == None:
            print "Could not load JSON"
            return None
        else:
            for num in js['comments']:
                comments.append(num['count'])
    
    return comments            
            
        
address = raw_input('Enter location: ')   

answer = parse_comment_counts(address)   

if answer == None:
    print "None was returned"

else:
    print "The sum is",sum(answer) 
        





