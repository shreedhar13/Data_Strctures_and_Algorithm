class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):  
        if data==self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else :
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else :
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
           elements+= self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
           elements+= self.right.in_order_traversal()

        return elements

    def search(self,data):
        if self.data == data:
            return True 
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data > self.data :  #wual cond is not there,,bcz  BST should contain UNIQUE value
            if self.right:
               return self.right.search(data)
            else:
                return False
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
        root=BinarySearchTreeNode(elements[0])
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root


if __name__ == '__main__':
    num=[17,4,1,20,9,23,18,34]
    num_tree=build_tree(num)
    print(num_tree.in_order_traversal())
    print(num_tree.search(1))

    strdata=['India','Pak','Germ','China','UK','USA','ENg']
    obj=build_tree(strdata)
    print(obj.in_order_traversal())
    print(obj.search('UK'))

    print(num_tree.find_max())