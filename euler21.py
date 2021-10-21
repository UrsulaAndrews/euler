def findDivisorsSum(num):
    divList = []
    for i in range(1, num):
        if num % i == 0:
            divList.append(i)
    sum = 0
    for n in divList:
        sum += n
    return sum

for n in range(1, 500):
    x = findDivisorsSum(n)
    y = findDivisorsSum(x)
    if x == y:
        print(str(n) + ',' + str(x) + ' ' + str(y))
    
