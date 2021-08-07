import re
# This file contain some functions to solve some problems about duplicate words in string.

# Find and remove deplicates of words in string
# what a word! you should not say that word -> what a word! you should not say that
def removeDuplicates(str):
    words = str.split()
    noDup = ''
    for word in words:
        if not re.search(r'\b' + word + r'\b', noDup):
            noDup += word + ' '
        else:
            pass
    return noDup

# find and remove all occurence of words that are duplicated
# what a word! you should not say that word -> what a ! you should not say that
def removeAllDuplicatedWords(str):
    words = str.split()
    noDup = ''
    for word in words:
        if not re.search(r'\b' + word + r'\b', noDup):
            noDup += word + ' '
        else:
            noDup = noDup.replace(word, '')
    return noDup

# find and return the first word that occured 2 or more times in string
# what a word! you should not say that word -> word
def firstWordDuplicated(str):
    words = str.split()
    noDup = ''
    for word in words:
        if not re.search(r'\b' + word + r'\b', noDup):
            noDup += word + ' '
        else:
            return word

# find the most time-occured word in string
# what a word! you should not say that word, that word is not polite! -> (word, 3)
def mostOccuredWord(str):
    occured = {}
    words = re.split(r'\W+', str)
    for word in words:
        if word not in occured:
            occured[word] = 1
        else:
            occured[word] += 1
    maxKey = max(occured, key = occured.get)
    maxValue = occured.get(maxKey)
    return maxKey, maxValue

str = 'what a word! you should not say that word'
print(removeDuplicates(str))
print(removeAllDuplicatedWords(str))
print(firstWordDuplicated(str))
print(mostOccuredWord(str))