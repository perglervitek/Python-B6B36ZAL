class MaxHeap:
    def __init__(self, data):
        self.data = data

    def getLeftChildIndex(self, index):
        return 2*index + 1

    def getRightChildIndex(self, index):
        return 2*index + 2

    def getMaxIndex(self, index):
        left = self.getLeftChildIndex(index)
        right = self.getRightChildIndex(index)
        print(right)
        if len(self.data)-1 < left:
            return None
        if len(self.data)-1 < right:
            return left
        if self.data[left] > self.data[right]:
            return left
        return right

    def siftDown(self, index):
        maxindex = self.getMaxIndex(index)
        if maxindex is not None and self.data[maxindex] > self.data[index]:
            self.data[maxindex], self.data[index] = self.data[index], self.data[maxindex]
            self.siftDown(maxindex)
    
    def heapify(self):
        for i in range(len(self.data) // 2, -1, -1):
            self.siftDown(i)
    
    def extractMax(self):
        mainData = self.data[0]
        self.data[0] = self.data.pop()
        self.siftDown(0)
        return mainData


mh = MaxHeap([15, 19, 10, 7, 17, 16])
print(mh.getMaxIndex(2))
print(mh.data)
