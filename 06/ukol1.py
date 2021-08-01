import random


array = []
for i in range(10):
    array.append(random.randint(1, 1000))


def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    return arr


def findMax(arr):
    max = arr[0]
    for i in arr:
        if(i > max):
            max = i
    return max


def findMin(arr):
    min = arr[0]
    for i in arr:
        if(i < min):
            min = i
    return min


def secondMax(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[1]

def secondLargest(arr):
    maxValue = findMax(arr)
    arr.remove(maxValue)
    return findMax(arr)


print(array)
print(swap(array, 1, 2))
print(findMax(array))
print(findMin(array))
print(secondMax(array))


# mx = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
# n = len(list1)
# for i in range(2, n):
#     if list1[i] > mx:
#         secondmax = mx
#         mx = list1[i]
#     elif list1[i] > secondmax and mx != list1[i]:
#         secondmax = list1[i]
