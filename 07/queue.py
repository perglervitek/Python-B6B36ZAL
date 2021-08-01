import car from Car

class Node:
    def __init__(seld, data):
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.nextNode
            curNode.newNode = newNode
        
        
    def pop(self):
        if self.head is None:
            return None
        dataToReturn = self.head.data
        self.head = self.head.nextNode
        return dataToReturn