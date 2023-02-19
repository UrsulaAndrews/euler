count = 0
for i in range(1,200):
    for n in range(1,200):
        if len(str(n ** i)) < i:
            continue
        elif len(str(n ** i)) == i:
            print(str(n) + " ^ " + str(i) + " = " + str(n ** i))
            count += 1
        else:
            break
        
print(count)
