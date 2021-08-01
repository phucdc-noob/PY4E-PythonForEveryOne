'''
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.*[$#@])                                  Require that at least one of #$@ special character appear anywhere in the string
.{6,12}                                      The password must be at least 6 characters long, but no more than 12
$                                            Match the end of the string.
'''



import re # regex

passes = input().split()

for p in passes:
    if re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$%@]).{6,12}$',p):
        print(p, sep=',') 