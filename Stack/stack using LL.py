class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev
        self.next = None
    
class Stack:
    def __init__(self, top):
        self.top = top
    
    def push(self, data):
        self.top.next = Node(data, self.top)
        self.top = self.top.next
    
    def pop(self):
        if self.isEmpty():
            return "! Stack is Empty"
        self.top = self.top.prev

        if self.top is not None:
            self.top.next = None
    
    def reveal(self):
        if self.isEmpty():
            return "! Stack is Empty"
        return self.top.data

    def isEmpty(self):
        return  not bool(self.top)
    
if __name__ == "__main__":
    stack = Stack(Node(10))
    for value in range(20, 101, 10):
        stack.push(value)
    
    while not stack.isEmpty():
        print(stack.reveal())
        stack.pop()
    
    
    