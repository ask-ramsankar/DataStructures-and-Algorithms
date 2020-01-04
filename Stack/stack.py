class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = stack()
    for i in range(10, 100, 10):
        s.push(i)
    print(s.peek())
    print('stack size: ', s.size())    
