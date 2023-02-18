def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lstOfPrimes = []
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
  
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            lstOfPrimes.append(p)
  
def getRotation(n):
    rot = set(())
    num = str(n)
    for i in range(len(num)):
        num = num[1:] + num[0]
        rot.add(int(num))
    return rot
    

num = 1000000
SieveOfEratosthenes(num)
setOfPrimes = set(lstOfPrimes)
circ = set(())

for n in lstOfPrimes:
    test = getRotation(n)
    if test.issubset(setOfPrimes):
        circ.update(test)
print(len(circ))
