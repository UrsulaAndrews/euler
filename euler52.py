n = 125874

for n in range(1,1000000):
    if set(str(n)) == set(str(n * 2)) == set(str(n * 3)) == set(str(n * 4)) == set(str(n * 5)) == set(str(n * 6)):
            print(n)

