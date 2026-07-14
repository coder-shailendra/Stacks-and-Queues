class queue:
    def __init__(self):
        self.q = []
        self.front = -1
    def push(self,x):
        if self.front ==-1:
            self.front = 0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x = self.q[self.front]
        self.front +=1
        if self.front == len(self.q):
            self.front -1
            self.q = []
        return x
    def getfront(self):
        if len(self.q)== 0:
            return -1
        return self.q[self.front]
    def size(self):
        if self.front == -1:
            return 0
        return len(self.q)-self.front
queue = queue()
queue .push(5)
queue .push(4)
queue .push(3)
queue .push(1)
print(queue.getfront())
queue.pop()
print(queue.getfront())
print(queue.size())