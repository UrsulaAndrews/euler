import sieve

def formula(p, s):
    return p + 2 * s**2

primes = sieve.SieveOfEratosthenes(6000)
composites = []
for i in range(6000):
    if i not in primes and i % 2 != 0:
        composites.append(i)
        
compositeCompare = set(())


for composite in composites:
    foundIt = False
    for p in primes:
        for i in range(1000):
            if formula(p, i) == composite:
                compositeCompare.add(composite)
                foundIt = True
                break
            if foundIt: break


z = set(composites).difference(compositeCompare)
print(z)
