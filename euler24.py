from itertools import permutations

perm = list(permutations([0,1,2,3,4,5,6,7,8,9]))

mill = perm[999999]

strmill = ""
for n in mill:
    strmill += str(n)

print(strmill)
