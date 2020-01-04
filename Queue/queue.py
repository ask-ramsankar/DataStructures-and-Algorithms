class queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, value):
        self.items.insert(0, value)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    q = queue()
    for i in range(10, 100, 10):
        q.enqueue(i)
    
    print(q.size())
    q.dequeue()
    print(q.size())