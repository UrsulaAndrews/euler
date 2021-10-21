fibonSeq = [1, 1]
while len(str(fibonSeq[-1])) < 1000:
    seq = fibonSeq[-2] + fibonSeq[-1]
    fibonSeq.append(seq)

print(fibonSeq[-1])
print(len(str(fibonSeq[-1])))
x = fibonSeq[-1]
ans = fibonSeq.index(x) + 1

print(ans)
