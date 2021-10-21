import time

def numdivisors(triangle):
  factors = 0
  for i in range(1, int((triangle ** 0.5)) + 1):
    if triangle % i == 0:
      factors += 1
  return factors * 2

def maxtriangledivisors(max):
  i = 1
  triangle = 0
  while i > 0:
    triangle += i
    if numdivisors(triangle) >= max:
      print('it was found number', triangle,'triangle', i, 'with total of ', numdivisors(triangle), 'factors')
      return triangle
    i += 1

startTime=time.time()
maxtriangledivisors(500)
print(time.time()-startTime)
