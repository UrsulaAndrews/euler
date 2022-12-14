def decimalToBinary(n):
    return bin(n).replace("0b", "")

def reverseString(x):
  return x [::-1]

sum = 0


for i in range(1000000):
    if str(i) == reverseString(str(i)) and decimalToBinary(i) == reverseString(decimalToBinary(i)):
        print(i)
        sum += i

print(sum)
