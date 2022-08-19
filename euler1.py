mult35 = []

for n in range (1,1000):
    if n % 3 == 0 or n % 5 == 0:
        mult35.append(n)


print(sum(mult35))
