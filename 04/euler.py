def fact(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result
 
def euler(iter):
     res = 0
     for i in range(iter):
        res += (1/fact(i))

     return res
    
print(euler(10))