class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.main = None
        self.checkedNodes = 1

    def insert(self, value):
        if self.main is None:
            self.main = Node(value)
        else:
            currVal = self.main
            isLooping = True
            while isLooping:
                if value > currVal.value:
                    if currVal.right is not None:
                        currVal = currVal.right
                    else:
                        currVal.right = Node(value)
                        isLooping = False
                else:
                    if currVal.left is not None:
                        currVal = currVal.left
                    else:
                        currVal.left = Node(value)
                        isLooping = False

    def fromArray(self, array):
        for item in array:
            self.insert(item)

    def search(self, value):
        self.checkedNodes = 0
        currVal = self.main

        while currVal is not None:
            self.checkedNodes += 1
            if value == currVal.value:
                return True
            elif currVal.value > value:
                currVal = currVal.left
            elif currVal.value < value:
                currVal = currVal.right
        return False

    def min(self):
        self.checkedNodes = 1
        currVal = self.main
        while currVal.left is not None:
            self.checkedNodes += 1
            currVal = currVal.left

        return currVal.value

    def max(self):
        self.checkedNodes = 1
        currVal = self.main
        while currVal.right is not None:
            self.checkedNodes += 1
            currVal = currVal.right

        return currVal.value

    def visitedNodes(self):
        return self.checkedNodes


# bst2 = BinarySearchTree()
# bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

# print(bst2.search(5))
# print(bst2.visitedNodes())
# print(bst2.search(7))
# print(bst2.visitedNodes())
# print(bst2.search(6))
# print(bst2.visitedNodes())
# print(bst2.search(10))
# print(bst2.visitedNodes())
# print("MIN: " + str(bst2.min()))
# print(bst2.visitedNodes())
# print("MAX: " + str(bst2.max()))
# print(bst2.visitedNodes())
