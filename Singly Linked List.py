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

     
    # Method for  inserting at the end of a LL

    def insert_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)

        current = self.head

        while current.get_next() != None:
            current = current.get_next()
        
        current.set_next(new_node)
        self.length += 1

    # Method for inserting at any position in LL

    def insert_at_position(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        elif pos == 0:
            self.insert_at_end(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            count = 1
            current = self.head
            while count < pos-1:
                count += 1
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            self.length += 1

    # Method to delete the first node of LL

    def delete_from_beginning(self):
        if sel.length == 0:
            print('The list is empty')
        else:
            self.head = self.head.get_next()
            self.length -= 1
    
    # Delete the last node of LL

    def delete_last_node(self):
        if self.length ==0:
            print("The list is empty")
        else:
            currentnode = self.head
            prevnode = self.head

            while currentnode.get_next() != None:
                prevnode = currentnode
                currentnode = currentnode.get_next()
            
            prevnode.set_next(None)
            self.length -= 1

    # Delete by node from LL

    def delete_by_node(self,node):
        if self.length == 0:
            raise ValueError('List is Empty')
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.length -= 1

    # Delete by data from LL

    def delete_by_data(self,value):
        currentnode = self.head
        prevnode = self.head

        while currentnode.get_next() != None or currentnode.get_data() != value:
            if currentnode.get_data() == value:
                prevnode.set_next(currentnode.get_next())
                self.length -= 1
                return
            else:
                prevnode = currentnode
                currentnode = currentnode.get_next()
            print("The value provided is not present.")

    # Method to delete a node at a particular location

    def delete_at_position(self,pos):
        count = 0
        currentnode = self.head 
        prevnode = self.head
        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter a valid position.')
        else:
            while currentnode.next != None or count < pos:
                count += 1
                if count == pos:
                    prevnode.set_next(currentnode.get_next())
                    self.length -= 1
                    return 
                else:
                    prevnode = currentnode
                    currentnode = currentnode.get_next()

























        