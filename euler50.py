import sieve

val = 1000000


def addEmUp(addends):
    total = 0
    for n in addends:
        total += n
    return total

primes = sieve.SieveOfEratosthenes(val)

topCount = 0
topRun = []
for j in range(0,len(primes)):
    runningTotal = 0
    addendsList = []
    for i in primes[j:]:
        runningTotal += i
        addendsList.append(i)
        if runningTotal < val and len(addendsList) > 1 and runningTotal in primes:
            if len(addendsList) > topCount:
                topCount = len(addendsList)
                topRun = addendsList.copy()
print(topCount)
print(topRun)
print(addEmUp(topRun))
        
