import re
import sqlite3

# connect to DNSList.txt
try:
    inFile = open('DNSList.txt', 'r')  # r read, w write, a append
    lines = inFile.readlines()
except:
    print('File DNSList.txt not found!')
    exit(-1)

# connect to database
conn = sqlite3.connect('DNSList.sqlite')
# drop table if exists and create new one instead
# IP must be unique
conn.executescript(
    '''
    drop table if exists DNS;
    
    create TABLE DNS (
        IP not null primary key unique,
        Reliability INTEGER,
        Description not null
    );
    '''
)

ip = reli = des = None
# read DNSList.txt line by line
for line in lines:
    # split line into many fields
    inputs = re.split('\s+', line)
    if inputs[0] == 'IP':
        ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', inputs[2])[0]
    elif inputs[0] == 'Reliability:':
        reli = int(re.search(r'\d{1,3}', inputs[1])[0])
        if reli >= 50:
            des = 'Normal'
        else:
            des = 'Low'
        conn.execute('insert into DNS values (?, ?, ?)', (ip, reli, des))
conn.commit()

table = conn.execute("SELECT * FROM DNS ORDER BY Reliability DESC")
print('DNS server list:')
print('IP\t\tReliability\tDescription')
for row in table:
    print(*row, sep='\t\t')
# close the connections
conn.close()
inFile.close()