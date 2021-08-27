import re
import sqlite3

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'Student.txt'
            inFile = open(filename, 'r') # cursor
            lines = inFile.readlines() # [dong1, dong2, ..., dong n]
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')


lines = getLines()
conn = sqlite3.connect('Student.sqlite')
conn.executescript(
    '''
    drop table if exists Student;
    create table Student (
        Name not null,
        Course not null,
        Grade integer not null,
        Description not null
    );
    '''
)

for line in lines:
    des = ''
    fields = re.split(r'\s+', line)
    if fields[0] == 'Course':
        continue
    if int(fields[2]) >= 50:
        des = 'Pass'
    else:
        des = 'Fail'
    conn.execute('insert into Student values (?, ?, ?, ?);', (fields[1], fields[0], int(fields[2]), des))
conn.commit()
tables = conn.execute('select * from Student order by Grade desc;')
print('Student list')
print('Name\t\t\tCourse\t\tGrade\t\tDescription')
for row in tables:
    print('%s\t\t\t%s\t\t%d\t\t%s' % (row[0], row[1], row[2], row[3]))