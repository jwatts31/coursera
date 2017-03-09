'''
Welcome Justin W from Using Python to Access Web Data

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://python-data.dr-chuck.net/geojson
This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

$ python solution.py
Enter location: South Federal University 
Retrieving http://...
Retrieved 2101 characters
Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok 
Turn In

Please run your program to find the place_id for this location:

University of West Florida
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJWWc ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.
'''

import urllib 
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

def find_location(address):
    
    #Initialize variable
    place_id = None
    
    #Check the address
    if len(address) < 1:
        print "Address is invalid, please enter a valid URL"
        return None
    else:
        try:
            url =  serviceurl + urllib.urlencode({'sensor':'false','address': address}) 
            #print "Retrievin",url
            uh = urllib.urlopen(url)
        except:
            print "Unable to obtain URL"
            return None
        
        data = uh.read() 
        
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
            if 'error' in js:
                print "Location does not exist"
                return None
            else:
                #print json.dumps(js, indent=4)
                place_id = js['results'][0]['place_id']
    
    if place_id == None:
        print "None was returned"
        return None

    else: 
        return place_id           
            