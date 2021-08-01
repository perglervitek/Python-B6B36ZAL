import math  

def newtonPi(init):
    x = init - (math.sin(init)/math.cos(init))
    while (x != init):
        init = x
        x = init - (math.sin(init)/math.cos(init))
    return init

def leibnizPi(iterations):
    res = 0
    for i in range(iterations):
        res += (-1)**i/(2*i+1)
    return float(res*4)


def nilakanthaPi(iterations):
    res = 3
    operation = 1
    n = 2
    for i in range(1,iterations):
        res += (4 / (n *(n+1)*(n+2))) * operation
        n +=2
        operation *= -1
    return float(res)
