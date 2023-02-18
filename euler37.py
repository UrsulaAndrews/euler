lstOfPrimes = []
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
  
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):  
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1  
    for p in range(2, num+1):
        if prime[p]:
            lstOfPrimes.append(p)

def truncate(n):
    truncSet = set(())
    num = str(n)
    num2 = str(n)
    truncSet.add(int(num))
    #Cut from left
    for i in range(len(num)-1):
        num = num[1:]
        truncSet.add(int(num))
    #Cut from right
    for i in range(len(num2)-1):
        num2 = num2[:-1]
        truncSet.add(int(num2))
    return truncSet

SieveOfEratosthenes(1000000)
primes = set(lstOfPrimes)
trPrimes = []

for i in lstOfPrimes:
    if i > 10:
        test = truncate(i)
        if test.issubset(primes):
            trPrimes.append(i)
print(trPrimes)

sumPrimes = 0
for i in trPrimes:
    if i > 9:
        sumPrimes += i
print(sumPrimes)
