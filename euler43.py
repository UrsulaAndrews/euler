import itertools
n = (1,4,0,6,3,5,7,2,8,9)

    
def breakdown(n):
    n = list(map(str, n))
    if int(n[1] + n[2] + n[3]) % 2 == 0:
        if int(n[2] + n[3] + n[4]) % 3 == 0:
            if int(n[3] + n[4] + n[5]) % 5 == 0:
                if int(n[4] + n[5] + n[6]) % 7 == 0:
                    if int(n[5] + n[6] + n[7]) % 11 == 0:
                        if int(n[6] + n[7] + n[8]) % 13 == 0:
                            if int(n[7] + n[8] + n[9]) % 17 == 0:
                                return True
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False
    else: return False

arr = [1,2,3,4,5,6,7,8,9,0]
pans = list(itertools.permutations(arr,10))
substr = []

for p in pans:
    if breakdown(p):
        pstr = ""
        for pd in p:
            pstr += str(pd)
        substr.append(int(pstr))
print(substr)

tot = 0
for n in substr:
    tot += n
print(tot)

