def badCancel(n, d):
    nn = str(n)[0]
    nd = str(d)[-1]
    if str(n)[-1] == str(d)[0] and int(nd) != 0:
        simp = int(nn) / int(nd)
    else:
        simp = 0
    return simp

def findLCM(a, b):
    r = 0
    lcm = 0
    r = a if a > b else b
    for i in range(1, r):
        if a % i == 0 and b % i == 0:
            lcm = i
    return(lcm)

pn = 1
pd = 1

for n in range(11, 100):
    for d in range(11, 100):
        if n/d == badCancel(n, d) and n/d < 1:
            print(n, d)
            print(n/d)
            print(badCancel(n, d))
            print("\n")
            pn *= n
            pd *= d
            
print(pn , pd)

print(findLCM(pn,pd))
print(pd/findLCM(pn,pd))
