n = 0
fSequence = [1, 2]
sum = 0

while n < 4000000:
    n = fSequence[-1] + fSequence[-2]
    fSequence.append(n)

for num in fSequence:
    if num % 2 == 0:
        sum += num
print(sum)
