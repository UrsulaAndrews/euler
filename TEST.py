def prime_eratosthenes(n):
    not_prime_list = []
    prime_list = []
    i = 2
    for i in range(2, n+1):
        if i not in not_prime_list:
##            print (i)
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                not_prime_list.append(j)
    return prime_list

plist = prime_eratosthenes(1000000)
print(str(len(plist)))
print(str(plist[3]))
