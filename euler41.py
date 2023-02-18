import sieve

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
lstPrimes = primes(7654321)

def isPandigital(n):
    num = str(n)
    if str(0) in num:
        return False
    pan = [False] * len(num)    
    for d in num:
        try:
            pan[int(d)-1] = True
        except IndexError:
            return False
    if False in pan:
        return False
    else:
        return True

i = 0
for x in reversed(lstPrimes):
    if isPandigital(x):
        print(x)
        break

