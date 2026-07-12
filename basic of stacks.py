class stack:
    def __init__(self):
        self.st = []
    def push(self,x):
        self.st.append(x)
    def pop(self):
        if len(self.st)==0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x
    def top(self):
        if len(self.st)== 0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.st)
stack = stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(9)
print(stack.pop())
print(stack.top())
print(stack.size())