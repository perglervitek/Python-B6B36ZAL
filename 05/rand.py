import random

arr = []
for i in range(10):
    arr.append(random.randint(1,1000))

    
def maxValue(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

print(maxValue(arr))