import re
# password filter
'''
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.*[$#@])                                  Require that at least one of #$@ special character appear anywhere in the string
.{6,12}                                      The password must be at least 6 characters long, but no more than 12
$                                            Match the end of the string.
'''
def pass_filter(pwd):
    return re.findall(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$%@]).{6,12}$', pwd)

# IP filter
'''
r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
'''
def ip_filter(ip):
    return re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ip)

# Email address filter
'''
r'\S+@\S+'
'''
def mail_filter(mail):
    return re.findall(r'\S+@\S+', mail)

# Date filter
'''
with dd/mm/yyyy format: (10-11-1966 or 10/11/1966)
    r'\d{2}[-/]\d{2}[-/]\d{4}'
with yyyy/mm/dd format: (1966-11-10 or 1966/11/10)
    r'\d{4}[-/]\d{2}[-/]\d{2}'
'''    
def date_filter(date):
    return re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', date)