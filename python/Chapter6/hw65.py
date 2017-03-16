'''
6.5 Write code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
'''
def covertToFloat(text):
    
    #Find the pos of the colon
    post_semi_colon = text.find(':')

    #slice from the colon to the end of the string
    extract_num = text[post_semi_colon+1:]

    try:
        #Strip the white space and covert to a float
        num = float(extract_num.strip())

    except:
        print "Could not covert number to a float"
    
    return num
    
# text given by hw    
text = "X-DSPAM-Confidence:    0.8475";

#call function
num = covertToFloat(text)

print num

