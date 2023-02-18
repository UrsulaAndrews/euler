maxsum = 0

for a in range(101):
    for b in range(101):
        pw = str(a ** b)
        tot = 0
        for n in pw:
            tot += int(n)
        if tot > maxsum:
            maxsum = tot
print(maxsum)
        
