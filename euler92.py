def oktry(n):
    if n == 1:
        return 1
    elif n == 89:
        return 89
    else:
        t = 0
        for i in str(n):
            t += int(i) ** 2
        return oktry(t)


ct89 = 0

for d in range(1, 10000001):
    if oktry(d) == 89:
        ct89 += 1
print(ct89)
