class  Node:
    def __init__(self,data=None,right=None,left=None):
        self.left=left
        self.data=data
        self.right=right

class doubly_linked_list:
    count=0
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        if self.count == 0:
           self.count+=1
           node=Node(data)
           self.head=node
        else:
            self.count+=1
            node=Node(data,right=self.head)
            self.head.left=node
            self.head=node

    def print_list(self):
        temp=self.head
        while temp:
            if temp.right == None:
                print(temp.data)
                temp=temp.right
            else:
                print(temp.data,'->',end='')
                temp=temp.right
        print('Total no of node in DLL is =>',self.count)
    
    def insert_at_end(self,data):
        if self.count == 0:
            self.count+=1
            node=Node(data)
            self.head=node
        else:
            temp=self.head
            while temp.right != None:
                temp=temp.right
            self.count+=1
            node=Node(data)
            temp.right=node
            node.left=temp

    def insert_at_random(self,data,pos):
        i=1
        #1st node is at 1st position,2nd node is at 2nd postion-->ie;we rae not taking 1st node at 0th position
        if pos <= 1:
            self.insert_at_beg(data)
        elif pos >= self.count:
            self.insert_at_end(data)
        else:
            temp=self.head
            while i != pos:
                temp=temp.right
                i+=1
            node=Node(data)
            temp.left.right=node
            node.left=temp.left
            node.right=temp
            temp.left=node
            self.count+=1
    def print_list_in_reverse(self):
        temp=self.head
        while temp.right != None:
            temp=temp.right
        while temp.left != None:
            print(temp.data,'<-',end=' ')
            temp=temp.left
        print(temp.data,end='')

if  __name__ == '__main__':
    dll=doubly_linked_list()
    dll.insert_at_beg(10)
    dll.insert_at_beg(20)
    dll.insert_at_beg(30)
    dll.insert_at_beg(40)
    dll.insert_at_end(5)
    dll.insert_at_random(69,3)
    dll.print_list()
    dll.print_list_in_reverse()


     