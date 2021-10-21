import re

nameFile = open('p022_names.txt')
nameContents = nameFile.read()
nameList = nameContents.split('","')
nameList.sort()
trialList = nameList[1:100]

def getNameScore(name):
    sum = 0
    for letter in name:
        sum += alphaScores[letter]
    return sum

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphaScores = {}
alphaScores['"'] = 1
i = 1
for letter in alpha:    #Create alphaScores dictionary
    alphaScores[letter] = i
    i += 1

bigSum = 0
for name in nameList:
    i = 1
    bigSum += (getNameScore(name) * (i))
    

print(bigSum)
