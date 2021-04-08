"""
Basic LinkedList with insertFirst, insertLast & printData methods
"""


class Node: 
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self): 
        self.head = None

    def insertFirst(self, data):
        """ Inserts data at the head of the LinkedList"""
        nodeFirst = Node(data, next=self.head)
        self.head = nodeFirst
        return self

    def insertLast(self, data): 
        """Inserts data at the end in the LinkedList"""
        newNode = Node(data)
        if(self.head):  
            current = self.head
            while(current.next): 
                current = current.next
            current.next = newNode
        else: #The LinkedList is empty 
            self.head = newNode

    def printData(self): 
        """Prints all of the data of the LinkedList"""
        current_Node = self.head
        while(current_Node): 
            print(current_Node.data)
            current_Node = current_Node.next

    
