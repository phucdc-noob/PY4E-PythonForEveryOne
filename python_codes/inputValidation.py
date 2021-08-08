# this file contain some shit about input validations like int, float, mail
# remember to import re

import re

def isInt(num):
    if re.match(r'^[-+]?([0-9]|[0-9].0)+$', num.strip()):
        return True
    return False

def isFloat(num):
    if re.match(r'^[-+]?([0-9]|[0-9].[0-9]{1,})+$', num.strip()):
        return True
    return False

def isMail(mail):
    if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mail.strip()):
        return True
    return False