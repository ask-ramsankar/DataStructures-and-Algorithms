# creates a node for stack
class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev
        self.next = None
    
class Stack:
    # initialize the stack object with the top node
    def __init__(self, data):
        self.top = Node(data)    
    
    # push the data to the stack
    def push(self, data):
        self.top.next = Node(data, self.top)
        self.top = self.top.next
    
    # deletes the top node from the stack
    def pop(self):
        if self.isEmpty():
            return "! Stack is Empty"
        self.top = self.top.prev
        
        # To check if stack has a prev node or not
        if self.top is not None:
            self.top.next = None
    
    # returns the data in the top node
    def reveal(self):
        if self.isEmpty():
            return "! Stack is Empty"
        return self.top.data
    
    # To check whether the stack is empty or not
    def isEmpty(self):
        return  not bool(self.top)
    
if __name__ == "__main__":
    stack = Stack(Node(10))
    for value in range(20, 101, 10):
        stack.push(value)
    
    while not stack.isEmpty():
        print(stack.reveal())
        stack.pop()
    
    
    
