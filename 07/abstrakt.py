from car import Car


class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

    def isEmpty(self):
        # return self.size() == 0
        # return len(self.data) == 0
        return not self.data

    def printItems(self):
        for i in range(self.size()):
            print(self.data[i])


myStack = Stack()
myStack.push(Car("Skoda", 630000))
myStack.push(Car("Cupra", 630000))
myStack.push(Car("Mazda", 460000))
myStack.push(Car("Audi", 860000))

myStack.printItems()

print('------------------------------------')

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

print(myStack.isEmpty())



