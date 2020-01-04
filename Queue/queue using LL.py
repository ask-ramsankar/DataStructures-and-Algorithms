# Node of the queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Initialize the queue with the first node
    def __init__(self, data):
        self.first = Node(data)
    
    # add a node to the queue at last
    def enqueue(self, data):
        current = self.first

        if current is None:
            self.first = Node(data)
        else:
            while current.next:
                current = current.next
            current.next = Node(data)
    
    # deletes first node from the queue
    def dequeue(self):
        self.first = self.first.next
    
    # return the data in the first node
    def reveal(self):
        return self.first.data
    
    # check whether the queue is empty or not
    def isEmpty(self):
        return not bool(self.first)
    

if __name__ == "__main__":
    queue = Queue(10)
    for data in range(20, 101, 10):
        queue.enqueue(data)
    
    while not queue.isEmpty():
        print(queue.reveal())
        queue.dequeue()
    