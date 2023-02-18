import sieve

def quad(n, a, b):
    return n**2 + (a * n) + b

primes = sieve.SieveOfEratosthenes(10000)


for a in range(-10, 10):
    for b in range(-10, 10):
        count = 0
        for n in range(-10, 10):
            if quad(n, a, b) in primes:
                print(str(quad(n, a, b)) + " n = " + str(n) + " a = " + str(a) + " b = " + str(b))
                count += 1
            print(count)
           
        
