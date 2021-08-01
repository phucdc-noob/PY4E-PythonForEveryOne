import re
import sqlite3

#connect to data.txt
inFile = open('C:\\Users\\phucb\\Documents\\python_codes\\data.txt', 'r')
lines = inFile.readlines()
cnt = 0

#connect to database
conn = sqlite3.connect('dbFPT.sqlite')
#drop table if exists and create new one instead
#IDs must be unique
conn.executescript(
    '''
    drop table if exists InFos;
    
    create TABLE InFos (
        ProCode INTEGER not null primary key unique,
        Deleted not null
    );
    '''
)

#read data.txt line by line 
for line in lines:
    #split line into many fields
    inputs = re.split('\s+', line) # \s la space \s+
    #check if the first field is ID (integer)
    if re.match('\d', inputs[0]): # \d la integer
        #add values to database
        conn.execute("INSERT INTO InFos VALUES (?, ?)", (int(inputs[0]), inputs[3]))
        #commit the command
        conn.commit()
        cnt+=1

print(cnt)
#print the top 3 highest IDs in descending mode, use fetch all to get output of command
print(conn.execute("SELECT ProCode,Deleted FROM InFos ORDER BY ProCode DESC LIMIT 3").fetchall())       
#close the connections
conn.close()
inFile.close()