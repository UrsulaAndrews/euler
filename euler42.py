def isTriangle(n):
    return int((.5 * n) *(n + 1))

triangleList = []
for i in range(100):
    triangleList.append(isTriangle(i))
    
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("C:\\Users\J\Desktop\pyScripts\Euler\p042_words.txt", "r")
wordData = f.read()
wordList = wordData.replace('"','').split(',')
triangleWords = []

for word in wordList:
    wrdpts = 0
    for letter in word:
        wrdpts += alpha.index(letter) + 1
    if wrdpts in triangleList:
        print(word + ": " + str(wrdpts))
        triangleWords.append(word)


print(triangleList)

print(len(triangleWords))
