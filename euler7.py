def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    finalPrime = []
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers & return the sum
    for p in range(2, n+1):
        if prime[p]:
##            print(p)
            finalPrime.append(p)
    return finalPrime

p20 = SieveOfEratosthenes(20)
print(p20[5])
