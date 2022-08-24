class Queue:
    # createQueue
    def __init__(self, n): # n: queue의 사이즈
        self.size = n
        self.items = [None] * n
        self.front = -1
        self.rear = -1

    def enQueue(self, item):  # item: queue에 들어갈 데이터
        if self.isFull():
            print("Queue is full")
        else:
            self.rear += 1
            self.items[self.rear] = item
    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.front += 1
            item = self.items[self.front]
            self.items[self.front] = None
            return item

        """    
        self.front += 1
            return self.items[self.front]
        """



    def isEmpty(self):
        # if self.front == self.rear:
        #     return True
        # else:
        #     return False
        return self.rear == self.front
    def isFull(self):
        if self.rear == self.size - 1:
            return True
        else:
            return False
    def Qpeek(self):
        return self.items[self.front]



q = Queue(3)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
print(q.items)
print(q.deQueue())
print(q.items)
print(q.deQueue())
print(q.items)
print(q.deQueue())
print(q.items)


