def reverseList(arr):
  if len(arr) == 0:
    return arr
  resultArr = reverseList(arr[1:])
  resultArr.append(arr[0])
  return resultArr

def revList(list, array = []):
    if len(list) >= 1:
        array.append(list[-1])
        revList(list[:-1])
    return array

def reverse_List(lst):
    if len(lst) == 1:
        return lst
    return lst[-1:] + reverse_List(lst[:-1])

print(reverseList([10, 20, 30, 40, 50]))
print(revList([10, 20, 30, 40, 50]))
print(reverse_List([10, 20, 30, 40, 50]))