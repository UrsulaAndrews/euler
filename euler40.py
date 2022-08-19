irrdec = "."
i = 1

while len(irrdec) < 1000001:
    irrdec += str(i)
    i += 1

eu = int(irrdec[1]) * int(irrdec[10]) * int(irrdec[100]) * int(irrdec[1000]) * int(irrdec[10000]) * int(irrdec[100000]) *int(irrdec[1000000])
print(str(eu))
    
    
