def exponents(base, exponent):
    sum = 0
    power = str(base ** exponent)
    print(power)
    for n in power:
        sum += int(n)
    print(sum)

exponents(2, 1000)    
