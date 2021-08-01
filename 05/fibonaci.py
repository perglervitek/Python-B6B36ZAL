def fiboList(n):
    if n <= 0:
        return('Spatne cislo')
    if n == 1:
        return[0]
    else:
        fiboArr = [0,1]
    for i in range(2,n+1):
        fiboArr.append(fiboArr[i-1] + fiboArr[i-2])
    return fiboArr
    
print(fiboList(10))