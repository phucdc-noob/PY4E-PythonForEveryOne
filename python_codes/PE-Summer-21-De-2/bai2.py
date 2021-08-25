import re

def getLines():
    while True:
        try:
            inFile = open('Trace.txt', 'r')
            lines = inFile.readlines()
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

if __name__ == '__main__':
    troubleshot = {}
    lines = getLines()
    for line in lines:
        fields = re.split(r'\s+', line)
        if fields[0] == 'Name:':
            provider = fields[1].split('-')[0]
            if provider not in troubleshot:
                troubleshot[provider] = 1
            else:
                troubleshot[provider] += 1
    print('Troubleshot wired LAN related issues:')
    for provider in sorted(troubleshot.keys()):
        print('%s: %d' % (provider, troubleshot[provider]))