def factorial(num):
    nFact = 1
    for i in range(num, 1, -1):
        nFact *= i
    return nFact

def sumIt(fact):
    sum = 0
    f = str(fact)
    for n in f:
        sum += int(n)
    return sum

print(sumIt(factorial(100)))
