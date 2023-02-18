def isPandigital(n):
    pan = [False] * 9
    num = str(n)
    for d in num:
        pan[int(d)-1] = True
    if False in pan:
        return False
    else:
        return True
prodTot = set(())

for i in range(9999):
    for j in range(9999):
        prod = i * j
        numberStr = str(i) + str(j) + str(prod)
        if str(0) in numberStr:
            continue
        elif len(numberStr) == 9 and isPandigital(numberStr):
            print(str(i) + " * " + str(j) + " = " + str(prod))
            prodTot.add(prod)

tot = 0            
for i in prodTot:
    tot += i
print(prodTot)
print(tot)
