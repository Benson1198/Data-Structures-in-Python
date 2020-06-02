# Node of a Singly Linked List
class Node:
    def __init__(self):
        self.data = data
        self.next = None
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next != None

    
    # Traverseing Lined List

    def list_length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            # To print data
            # print(current.get_data()) 
            current = current.get_next()

        return count
    
    # Method for inserting node at beginning of LL

    def insert_at_beginning(self,data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node

        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1

     


