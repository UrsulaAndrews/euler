def findDivisorsSum(num):
    divList = []
    for i in range(1, num):
        if num % i == 0:
            divList.append(i)
    return sum(divList)

amicable = set()

for n in range(10000):
    x = findDivisorsSum(n)
    y = findDivisorsSum(x)
    if n == y and x != y:
        amicable.add(n)
        amicable.add(x)

print(amicable)
print(sum(amicable))
