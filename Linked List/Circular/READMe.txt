Circular Linked List:
	Main different between this and singly or doubly is the last node in the list has None in the next part.
	But here It has the self.head value of the list.
	While accessing the values it will act like no ending circle.
	So we use self.tail to notice the last node in the list.