class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        current = self.head
        while current.next != None:
            current = current.next
        new_node = Node(value)
        new_node.previous = current
        current.next = new_node

    def display(self):
        current = self.head
        while current != None:
            print(current.value, end='<=>')
            current = current.next
        print()

    def delete(self,key):
        current = self.head
        while current != None:
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
            self.head = new
        else:
            current = self.head.next
            i = 1
            while current:
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
            self.head = self.head.next
        else:
            current = self.head.next
            i = 1
            while current:
                if i == index:
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
        while current:
            if current.value == key:
                return index
            index += 1
            current = current.next
        else:
            raise KeyError('Key not found')


if __name__ == '__main__':
    l=DoublyLinkedList()
    l.head=Node(10)
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