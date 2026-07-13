class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.length = 0
    def push(self,x):
        self.length +=1
        if self.top is None:
            self.top = Node(x)
            return
        else:
            newNode = Node(x)
            newNode.next = self.top
            self.top = newNode
    def pop(self):
        if self.top == None:
            return -1
        self.length -=1
        x = self.top.data
        self.top = self.top.next
        return x
    def gettop(self):
        if self.top == None:
            return -1
        return self.top.data
    def size(self):
        return self.length
stack = stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(9)
print(stack.size())
print(stack.pop())
print(stack.gettop())
