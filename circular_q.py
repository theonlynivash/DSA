class cq():
    def __init__(self, size):
        self.size = size
        self.q = [None]*size
        self.front = -1
        self.rear = -1
    def isfull(self):
        return (self.rear+1)%self.size == self.front
    def isempty(self):
        return self.front == -1 and self.rear == -1
    def enqueue(self,data):
        if self.isfull():
            print("OVER FLOW")
            return -1
        else:
            if self.isempty():
                self.front = 0
        self.rear = (self.rear+1)%self.size
        self.q[self.rear] = data
    def dequeue(self):
        if self.isempty():
            print("UNDER FLOW")
            return -1
        else:
            self.q[self.front] = None
            self.front = (self.front+1)%self.size
        if self.front == self.rear:
            self.rear = -1
            self.front = -1
    def display(self):  
        if self.isempty():
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.q[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()
cq1 = cq(5)
cq1.enqueue(10)
cq1.enqueue(20)
cq1.enqueue(30)
cq1.enqueue(40)
cq1.enqueue(50)
cq1.display()
cq1.dequeue()
cq1.dequeue()
cq1.display()
cq1.enqueue(60)
cq1.display()