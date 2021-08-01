#               Bubble
# for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if(arr[j] > arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def bubbleSort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if(arr[j] > arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

def swap1(data, x, y):
    data[y], data[x] = data[x], data[y]


def bubbleSort(data):
    for j in range(len(data)):
        wasSwap = False
        for i in range(1, len(data)-j):
            if(data[i] < data[i-1]):
                swap1(data, i, (i-2))
                wasSwap = True
        if not wasSwap:
            break
    return data


def selectionSort(data):
    for unsortedIndex in range(0, len(data)-1):
        minIndex = unsortedIndex
        for i in range(unsortedIndex + 1,len(data)):
            if data[i] < data[minIndex]:
                minIndex = i
        data[minIndex], data[unsortedIndex] = data[unsortedIndex], data[minIndex]
    return data


print(bubbleSort([3, 4, 9, 3, 5, 0, 7, 1]))
print(selectionSort([3, 4, 9, 3, 5, 0, 7, 1]))
