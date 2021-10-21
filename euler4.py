def palindroneCheck(str):
    is_palindrone = False
    if str[0] == str[-1]:
        if str[1] == str[-2]:
            if str[2] == str[-3]:
                is_palindrone = True
    else:
        is_palindrone = False
    return is_palindrone

i = 99
pal = 0

for i in range(1000, 101, -1):
    for j in range(1000, 101, -1):
        pal = i * j
        if palindroneCheck(str(pal)):
            print(str(i) + ' & ' + str(j) + ' = ' + str(pal))

