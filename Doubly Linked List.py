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

    
    # Insert Node at Beginning of Doubly Linked List

    def insert_at_beginning(self,data):
        new_node = Node(data,None,None)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node


    # Insert at the end of Doubly Linked List

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head

            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(data,None,current))
            self.tail = current.get_next()

    # Get node by index
    def get_node(self,index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.get_next() != None:
            currentNode = currentNode.get_next()
            if currentNode == Node:
                break
            i += 1
        return currentNode

    # Insert at given position in DLL
    def insert_at_given_position(self,index,data):
        new_node = Node(data)

        if self.head == None or index == 0:
            self.insert_at_beginning(data)
        elif index > 0:
            temp = self.get_node(index)

            if temp == None or temp.get_next() == None:
                self.insert_at_end(data)
            else:
                new_node.set_next(temp.get_next())
                new_node.set_prev(temp)
                temp.get_next().set_prev(new_node)
                temp.set_next(new_node)
