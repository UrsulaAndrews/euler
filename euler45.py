def triangle(n):
    t = (n * (n + 1))/2
    return t

def pentagonal(n):
    p = (n * (3*n - 1))/2
    return p

def hexagonal(n):
    h = n * (2 * n - 1)
    return h

tri = set(())
pent = set(())
hexa = set(())

for i in range(1,300000):
    tri.add(triangle(i))
    pent.add(pentagonal(i))
    hexa.add(hexagonal(i))

tph = tri.intersection(pent, hexa)
print(tph)
