def permutations(array):
    perms = []
    if len(array) == 0 or len(array) == 1:
        return [array]
    else:
        for key, firstItem in enumerate(array):
            remainingItems = array[key+1:] + array[:key]
            for permut in permutations(remainingItems):
                perms.append([firstItem] + permut)
    return perms


# print(permutations(['a', 'b', 'c', 'd']))
# print(permutations([1]))
# print(permutations([]))
# [['b', 'a', 'c', 'd'], ['b', 'c', 'a', 'd'], ['b', 'c', 'd', 'a'], ['c', 'a', 'b', 'd'], ['c', 'b', 'a', 'd'], ['c', 'b', 'd', 'a'], ['a', 'c', 'd', 'b'], ['c', 'a', 'd', 'b'], ['c', 'd', 'a', 'b'], ['c', 'd', 'b', 'a'], ['b', 'a','d', 'c'], ['b', 'd', 'a', 'c'], ['b', 'd', 'c', 'a'], ['a', 'd', 'b', 'c'], ['d', 'a', 'b', 'c'], ['d', 'b', 'a', 'c'], ['d', 'b', 'c', 'a'], ['a', 'd', 'c', 'b'], ['d', 'a', 'c', 'b'], ['d', 'c', 'a', 'b'], ['d', 'c', 'b', 'a']]