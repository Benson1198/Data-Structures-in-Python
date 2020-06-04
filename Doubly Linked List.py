class Node:
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def set_prev(self,prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    def __str__(self):
        return "Node [Data = {}]".format(self.data)  

    
    # Insert Node at Beginning od Doubly Linked List

    def insert_at_beginning(self,data):
        new_node = Node(data,None,None)

        if self.head == None:
            self.head = new_node
        else:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node