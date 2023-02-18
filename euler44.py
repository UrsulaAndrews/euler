def pentFormula(n):
    x = (n * (3*n - 1)) / 2
    return int(x)

pents = [pentFormula(x) for x in range(1, 5000)]

    
for i in range(len(pents)):
    for j in range(len(pents)):
        if pents[i] + pents[j] in pents:
            if pents[i] - pents[j] in pents:
                print(str(pents[i]) + " & " + str(pents[j]))
        

