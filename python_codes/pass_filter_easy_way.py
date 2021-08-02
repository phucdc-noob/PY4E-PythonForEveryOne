# Filter password using any()
# any() means require one or more
# not any() means 0
# check if not any() to check if there is at least 1 character as required
# not any(c.isdigit() for c in passwd) means if there are not any digit(0-9), so we can understand the concept here:
# if there are not any character is digit (0-9) or not any is lower (a-z) or not any is upper (A-Z) or not any is in specChar then the passFilter Fuction return False
# else return True (password matched all requires)

def passFilter(passwd):
    specChar = ['#', '@', '$']
    if len(passwd) < 6 or len(passwd) > 12 or not any(c.isdigit() for c in passwd) or not any(c.isupper() for c in passwd) or not any(c.islower() for c in passwd) or not any(c in specChar for c in passwd):
        return False
    return True

passes = input().split()
for passwd in passes:
    if passFilter(passwd):
        print(passwd)