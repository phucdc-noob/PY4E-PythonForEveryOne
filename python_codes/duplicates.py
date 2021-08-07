from enum import unique
import re

# Find and remove duplicate of characters in string
# aabbcc -> abc
def removeDuplicate(str):
    noDup = ''
    for char in str:
        if char in noDup:
            pass
        else:
            noDup += char
    return noDup

# delete all characters that occur 2 or more times in string
# aaabbc -> c
def removeCharsDuplicate(str):
    uniqueChars = {}
    result = str
    for char in result:
        if char in uniqueChars:
            result = result.replace(char, '')
        else:
            uniqueChars[char] = 1
    return result

# find the first character that occurs 2 or more times in string
# abcdabc -> a
def findFirstDuplicateChar(str): 
    uniqueChars = {}
    for char in str:
        if char in uniqueChars:
            return char
        else:
            uniqueChars[char] = 1

# find the character that occurs the most time in string
# aaabbc -> a occurs 3 time, b occurs 2 time, so the result is a
def findMostDuplicateChar(str):
    uniqueChar = {}
    for char in str:
        if char in uniqueChar:
            uniqueChar[char] += 1
        else:
            uniqueChar[char] = 1
    maxKey = max(uniqueChar, key = uniqueChar.get)
    maxValue = uniqueChar.get(maxKey)
    return maxKey, maxValue




str = 'python.is,suck?as.fuck'
print(removeDuplicate(str))
print(removeCharsDuplicate(str))
print(findFirstDuplicateChar(str))
print(findMostDuplicateChar(str))