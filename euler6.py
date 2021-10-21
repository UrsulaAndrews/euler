sumSquare = 0
squareSum = 0
for i in range(1, 101): #sum of squares
    sS = i**2
    sumSquare += sS

for i in range(1, 101):
    squareSum += i
squareSum **= 2

print(int(sumSquare))
print(int(squareSum))
print(int(squareSum - sumSquare))
