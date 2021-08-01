def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def factIter(n):
  res = 1
  for i in range(2, n + 1):
    res *= i
  return res

print(factIter(5))