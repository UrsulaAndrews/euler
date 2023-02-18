def isPandigital(n):
    pan = [False] * 9
    num = str(n)
    for d in num:
        pan[int(d)-1] = True
    if False in pan:
        return False
    else:
        return True

largest = 0
for i in range(1, 100000):
    conProd = ""
    for j in range(1,10):
        conProd += str(j*i)
        if len(conProd) < 9:
            continue
        elif len(conProd) == 9 and isPandigital(conProd):
            print(conProd)
            if largest < int(conProd):
                largest = int(conProd)
        else:
            break
    
print(largest)
