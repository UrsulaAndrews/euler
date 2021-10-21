import math

for a in range(1, 1000):
    for b in range(1, 1000):
        c = a**2 + b**2
        c = math.sqrt(c)
        if c.is_integer() and a + b + c == 1000:
            print(str(a) + ' + ' + str(b) + ' + ' + str(c) + ' = ' + str(a + b + c))
            print(str(a*b*c))
