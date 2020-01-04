class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=node(data)

    def display(self):
        current=self.head
        while current!=None:
            print(current.data, end='->')
            current=current.next
        print()

    def delete(self,key):
        prev=None
        current=self.head
        while current!=None:
            if current.data==key:
                prev.next=current.next
                return True
            else:
                prev=current
                current=current.next
        raise ValueError("key not found")

    def insertAt(self, index, value):
        new = node(value)
        if index == 0:
            new.next = self.head
            self.head = new
        else:
            prev = self.head
            current = self.head.next
            i = 1
            while current:
                if i == index:
                    new.next = current
                    prev.next = new
                    return
                else:
                    prev = current
                    current = current.next
                    i += 1
            else:
                raise IndexError('Index out of range')

    def deleteAt(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            i = 0
            while current:
                if i == index:
                    prev.next = current.next
                    return 
                else:
                    prev = current
                    current = current.next
                    i += 1
            else:
                raise IndexError('Index out of range')
        
    def reverse(self):
        current = self.head
        null = node(-1)

        while current:
            temp = null.next
            null.next = node(current.data)
            null.next.next = temp
            current = current.next      

        return null.next

    def reverseOn(self, k):
        current = self.head
        reversed_ll = None
        flag = True
        null = node(-1)

        while True:
            temp = current
            i = 0
            while temp and i < k:
                i += 1
                temp = temp.next
            
            if i == k:
                j = 0
                
                while j < k:
                    temp = node(current.data)
                    temp.next = null.next
                    null.next = temp
                    current = current.next
                    j += 1
                
                if flag:
                    reversed_ll = null.next
                    null = node(-1)
                    flag = False
                else:
                    temp = reversed_ll
                    while temp.next:
                        temp = temp.next
                    temp.next = null.next
                    null = node(-1)
                
            else:
                temp = reversed_ll
                while temp.next:
                    temp = temp.next
                temp.next = current
                return reversed_ll


    

if __name__ == '__main__':
    l=linkedlist()
    l.head=node(10)
    for i in range(20, 100, 10):
        l.append(i)
    l.display()
    l.delete(30)
    l.display()
    l.insertAt(0, 500)
    l.display()
    l.deleteAt(0)
    l.display()
    head = l.reverse()
    r = linkedlist()
    r.head = head
    r.display()
    head = l.reverseOn(5)
    r  = linkedlist()
    r.head = head
    r.display()

        


        
