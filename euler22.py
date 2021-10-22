import re

nameFile = open('p022_names.txt')
nameContents = nameFile.read()
nameContents = re.sub('"', '', nameContents)
nameList = nameContents.split(',')
nameList.sort()

def getNameScore(name):
    sum = 0
    for letter in name:
        sum += alphaScores[letter]
    return sum

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphaScores = {}
i = 1
for letter in alpha:    #Create alphaScores dictionary
    alphaScores[letter] = i
    i += 1

bigSum = 0
i = 1
for name in nameList:
    bigSum += getNameScore(name) * (nameList.index(name) + 1)
    

print(bigSum)
print(getNameScore('COLIN'))
print(nameList.index('COLIN'))
