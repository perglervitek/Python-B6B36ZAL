cars = ["Ford", "Audi", "Alfa","Romeo", "Skoda", "Toyota"]

def printItems(arr):
    for i in arr:
        print("Znacka",i)

def containsItem(searchText,arr):
    for i in arr:
        if searchText == i:
            return True
    return False

def addItem(item, arr):
    if(not containsItem(item,arr)):
        arr.append(item)
        return arr

def removeItem(item, arr):
    if(containsItem(item, arr)):
        arr.remove(item)
        return arr

def replaceItem(arr, item1, item2):
    if(containsItem(item1, arr)):
        for i in range(len(arr)):
            if arr[i] == item1:
                arr[i] = item2
    return arr

def findItem(arr):
    return arr

def reverseArr(arr):
    new = []
    for i in range(1, len(arr) +1):
        new.append(arr[-i])
    return new

    
# printItems(cars)
# print(containsItem('ford', cars))

cars = addItem('testik', cars)
print(cars)
print(replaceItem(cars, 'Skoda', 'fabia'))

print(reverseArr(cars))