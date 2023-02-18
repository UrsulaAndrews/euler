import math

def findDivisorsSum(num):
    divList = [1]
    for i in range(2, int(math.sqrt(num)+ 1)):
        if num % i == 0:
            divList.append(i)
            if i * i != num:
                divList.append(num/i)
    return sum(divList)

abundant = []
abundantSummers = set()
allNums = set([i for i in range(1, 28124)])

        
for x in range(1, 28126):
    if x < findDivisorsSum(x):
        abundant.append(x)

for i in range(len(abundant)):
    for j in range(len(abundant)):
        abundantSummers.add(abundant[i] + abundant[j])

        
diff = allNums.difference(abundantSummers)      
tot = 0
for i in diff:
    tot += i

print(tot)
    

