# i have designed this code
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class BST:
    count=0
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.count==0:
             self.count+=1
             node=Node(data)
             self.root=node
        else:
            temp=self.root
            prev=None
            while temp.data > data or temp.data < data:
                if temp.data > data:
                    prev=temp
                    temp=temp.left
                elif temp.data < data:
                    prev=temp
                    temp=temp.right
                if temp == None:
                    break
            
            if prev.left == None and prev.data > data:
                self.count+=1
                node=Node(data)
                prev.left=node
            elif prev.right == None and prev.data < data:
                self.count+=1
                node=Node(data)
                prev.right=node
    def inorder(self,root):
        
        if root != None:
            self.inorder(root.left)
            print(root.data,'->',end='')
            self.inorder(root.right)

    def search(self,data,root):
        
        if root.data == data:
            print('data is present')
        else:
            if root.data > data:
                temp=temp.left
                self.search(data)
            else:
                temp=root.right
                self.search(data)
if __name__ == '__main__':
    obj=BST()
    l=[100,50,35,70,71,36,21]
    for e in l:
        obj.insert(e)
    root=obj.root
    obj.inorder(root)
        



