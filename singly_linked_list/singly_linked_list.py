class Node: 
    def __init__(self, value):
        self.value = value
        self.next  = None 

# a linked list is not an array
class LinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None     

    def add_to_tail(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode 
        return 
        self.tail.next = newNode 
        self.tail = newNode

    def add_to_head(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode 
        return 
        self.head.next = self.head 
        self.head  = newNode

    def remove_head(self):
        if self.head is None: 
            return 
        self.head = self.head.next
    
    def remove_tail(self):
        if self.tail is None:
            return
        if self.head.next is None:
            self.head = None 
            self.tail = None

        pointer = self.head 
        while pointer.next is not self.tail:
            pointer = pointer.next

        self.tail = pointer      

    
         

        