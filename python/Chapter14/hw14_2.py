'''
WORK IN PROGRESS. MANY CHANGES STILL NEEDED BUT IT WORKS!


Counting Organizations
This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
'''

import sqlite3
import re

def create_table(sqllite_file_name):
    
    table_connction = {}
    
    try:
        conn = sqlite3.connect(sqllite_file_name)
        cur = conn.cursor()

        cur.execute('''
        DROP TABLE IF EXISTS Counts''')

        cur.execute('''
        CREATE TABLE Counts (org TEXT, count INTEGER)''')
        
        table_connction['connection'] = conn
        table_connction['cursor'] = cur
        
        return table_connction
        
    except:
        print "Failed to create table"
        
        return False


def get_emails(file_name):
    
    emails = []
    
    #set default is file_name is provided
    if ( len(file_name) < 1 ) : file_name = 'mbox-short.txt'

    with open(file_name,'r') as file_handler:
    
        for line in file_handler:
            if not line.startswith('From: '): 
                continue
            line = line.rstrip()
            
            domain = re.search("@([\w.]+)", line)
            email = domain.group(0)
            emails.append(email[1:])
            
    return emails

    
def insert_table(emails,table):

    for email in emails:
        
        table['cursor'].execute('SELECT count FROM Counts WHERE org = ? ', (email, ))
        row = table['cursor'].fetchone()
        if row is None:
            table['cursor'].execute('''INSERT INTO Counts (org, count) 
                    VALUES ( ?, 1 )''', ( email, ) )
        else : 
            table['cursor'].execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
                (email, ))
        # This statement commits outstanding changes to disk each 
        # time through the loop - the program can be made faster 
        # by moving the commit so it runs only after the loop completes
    table['connection'].commit()
        
def read_table(table):

    table_data = []
    
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
    
    for row in table['cursor'].execute(sqlstr):
        table_data.append((str(row[0]),row[1]))


    print "table data is",table_data
    return table_data


sqllite_file_name = 'emaildb.sqlite'
table = create_table(sqllite_file_name)

emails = get_emails('mbox.txt')

#print emails

insert_ret = insert_table(emails,table)

highest_count = read_table(table)

#print "highest count is",highest_count




