class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, value):
        current = self.head
        while current != self.tail:
            current = current.next
        new_node = Node(value)
        new_node.previous = current
        new_node.next = self.head
        current.next = new_node
        self.tail = new_node

    def display(self):
        current = self.head
        while current != self.tail:
            print(current.value, end='<=>')
            current = current.next
        print(self.tail.value)

    def delete(self,key):
        current = self.head
        while current != self.tail:
            if current.value == key:
                current.previous.next = current.next
                current.next.previous = current.previous
                break
            else:
                current = current.next

    def insertAt(self, index, value):
        new = Node(value)
        if index == 0:
            new.next = self.head
            new.previous = self.head.previous
            self.head = new
            if self.tail == self.head:
                self.tail = self.head
            else:
                self.tail.next = self.head
        else:
            current = self.head.next
            i = 1
            while current != self.head:
                if i == index:
                    new.next = current
                    current.previous.next = new
                    new.previous = current.previous
                    current.previous = new
                    return
                else:
                    current = current.next
                    i += 1
            else:
                raise IndexError('Index out of range')

    def deleteAt(self, index):
        if index == 0:
            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next
        else:
            current = self.head.next
            i = 1
            while current != self.head:
                if i == index:
                    if current == self.tail:
                        self.tail = current.previous
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return 
                else:
                    current = current.next
                    i += 1
            else:
                raise IndexError('Index out of range')
    
    def find(self, key):
        current = self.head
        index = 0
        while current != self.tail:
            if current.value == key:
                return index
            index += 1
            current = current.next
        else:
            if self.tail.value == key:
                return index
            else:
                return 'Key not found'


if __name__ == '__main__':
    l=CircularLinkedList()
    l.head = Node(10)
    l.tail = l.head
    for i in range(20, 100, 10):
        l.insert(i)
    l.display()
    l.delete(30)
    l.display()
    l.insertAt(0, 500)
    l.display()
    l.deleteAt(0)
    l.display()
    print(l.find(40))

    