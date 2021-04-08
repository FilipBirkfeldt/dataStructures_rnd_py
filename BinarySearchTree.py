
# Practice for building a binary search tree with some basic methods

class Binary_Search_Tree:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def addNode(self, data):
        if data == self.data:
            return # duplicate
        
        # Left-side of the BST 
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = Binary_Search_Tree(data)
            
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = Binary_Search_Tree(data)


    def find_Node(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.find_Node(val)
            else:
                return False

        if val > self.data:
            if self.rigth:
                return self.right.find_Node(val)
            else:
                return False

    def traversIn_order(self):
        data_list = []
        if self.left:
            data_list += self.left.traversIn_order()

        data_list.append(self.data)

        if self.right:
            data_list += self.right.traversIn_order()

        return data_list
    
    
    def hitta_maxValue(self):
        if self.right is None:
            return self.data
        return self.right.hitta_maxValue()
 
    
""" Building a actual tree! """
bt = Binary_Search_Tree(5)
import random 

for x in range(2,20): 
    x = x + random.randrange(-15,5)
    bt.addNode(x)

dataList = bt.traversIn_order()

[print(x) for x in dataList]