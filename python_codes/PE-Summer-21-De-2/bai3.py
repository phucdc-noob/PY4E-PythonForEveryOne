import sqlite3
import re

if __name__ == '__main__':
    try:
        inFile = open('Trace.txt', 'r')
        lines = inFile.readlines()
    except (FileNotFoundError, IOError):
        print('File not found or unreadable.')
    
    conn = sqlite3.connect('Trace.sqlite')
    # Name is unique
    # Drop table if exits
    conn.executescript(
        '''
            drop table if exists providers;
            create table providers(
                pname not null primary key,
                pcount int not null,
                pwarning not null
            );   
        '''
    )
    
    troubleshot = {}
    for line in lines:
        fields = re.split(r'\s+', line)
        if fields[0] == 'Name:':
            provider = fields[1].split('-')[0]
            if provider not in troubleshot:
                troubleshot[provider] = 1
            else:
                troubleshot[provider] += 1
    
    for provider in troubleshot.keys():
        pwarning = ''
        if troubleshot[provider] > 1:
            pwarning = 'High risk'
        else:
            pwarning = 'Normal'
        conn.execute('insert into providers values (?, ?, ?);', (provider, troubleshot[provider], pwarning))
    conn.commit()
    
    tables = conn.execute('select * from providers order by pcount desc;')
    print('Troubleshot wired LAN related issues:')
    print('%10s %5s %10s' % ('Provider', 'Count', 'Warning'))
    
    for row in tables:
        print('%10s %5d %10s' % (row[0], row[1], row[2]))
    conn.close()
    inFile.close()