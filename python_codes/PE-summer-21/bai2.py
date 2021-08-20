# regex
import re

locations = {}

while True:
    filename = input('Enter file: ') #string
    if not filename:
        filename = 'DNSList.txt'
    try: 
        inFile = open(filename, 'r') # cursor
        lines = inFile.readlines()
        break
    except:
        print('File not found. Please check.')

for line in lines:
    fields = re.split('\s+', line) # \s = space; field = ['<:', '']
    if fields[0] == 'Location:':
        if fields[1] not in locations:
            locations[fields[1]] = 1
        else:
            locations[fields[1]] += 1

print('DNS Server list:')
print('%10s%10s' % ('Country', 'Count'))
for key in sorted(locations.keys()):
   print('%10s%10d' % (key, locations[key]))
inFile.close()
# dict = {key:value}
# dict[key] = value