
class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.children=[]#which is list pointer/refrence to children,,(dynamic type casting)
        self.parent=None
    def add_child(self,child):
        child.parent=self 
        self.children.append(child)
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        spaces=' ' * self.get_level()*3
        prefix=spaces + '|---' if self.parent else ''
        print(prefix+self.data)
        if self.children:
         for child in self.children:
            child.print_tree()
    
def build_product_tree():
    root=TreeNode('Electronics')

    laptop=TreeNode('Laptop')
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('hp'))
    laptop.add_child(TreeNode('dell'))

    cell_phone=TreeNode('Cell_phone')
    cell_phone.add_child(TreeNode('iphone'))
    cell_phone.add_child(TreeNode('oneplus'))
    cell_phone.add_child(TreeNode('vivo'))

    television=TreeNode('television')
    television.add_child(TreeNode('a'))
    television.add_child(TreeNode('b'))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(television)

    return root

if __name__ == '__main__':
    root=build_product_tree()
    root.print_tree()