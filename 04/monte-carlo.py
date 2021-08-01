import random
def estimate(iterations):
    insideCircle = 0
    for i in range(iterations):
        x2 = random.uniform(-1,1)**2
        y2 = random.uniform(-1,1)**2
        zeroDistance = (x2 + y2)**1/2
        print(zeroDistance)
        if zeroDistance <= 1:
            insideCircle += 1
    return 4 * (insideCircle / iterations)
    

iter = int(input("Zadejte počet iterací: "))
print(estimate(iter))