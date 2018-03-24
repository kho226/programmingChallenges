'''
    Author: Kyle Ong   
    Date: 03/22/2018
    
    AVL Tree Class
    
    height ~> log(n)
    
    search ~> O(logn)
    

'''

class TreeNode(object):
    '''
        Author: Kyle Ong
        Date: 03/22/2018
        
        TreeNode Class
    
    '''
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1



class AVLTree(object):
    '''
        Author: Kyle Ong
        Date:03/22/2018 
        
        AVL Tree class
        
        insert()
        get_height()
        get_load()
        left_rotate()
        right_rotate()
        pre_order()
    
    '''
    
    def insert(self,key,root):
        
        if not root: return TreeNode(key)
        elif key < root.val: root.left = self.insert(key,root.left)
        else: root.right = self.insert(key,root.right)
            
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        
        load = self.get_load(root)
        
        if (load > 1 and key < root.left.val): return self.right_rotate(root)
        if (load > 1 and key > root.left.val):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if (load < -1 and key > root.right.val): return self.left_rotate(root)
        if (load < -1 and key < root.right.val):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_height(self,node):
        if not node: return 0
        return node.height
    
    def get_load(self,node):
        if not node: return 0
        load = self.get_height(node.left) - self.get_height(node.right)
        return load
    
    def left_rotate(self,x):
        y = x.right
        sub_tree = y.left
        
        y.left = x
        x.right = sub_tree
        
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        
        return y
    
    def right_rotate(self,x):
        
        y = x.left
        sub_tree = y.right
        
        y.right = x
        x.left = sub_tree
        
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        
        return y
    
    def pre_order(self,node):
        
        if not node: return
        
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)
        

    
def main():
    tree = AVLTree()
    
    root = None
    
    root = tree.insert(10,root)
    root = tree.insert(20,root)
    root = tree.insert(30,root)
    root = tree.insert(40,root)
    root = tree.insert(50,root)
    root = tree.insert(25,root)
    
    
    tree.pre_order(root)
    #tree.pre_order(root)
    
    
main()