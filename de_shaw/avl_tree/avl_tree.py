'''
    Author: Kyle Ong
    Date: 03/20/2018

    avl tree

    insert: log(n)
    left_rotate: O(1)
    right_rotate: O(1)
    get_height: O(1)
    get_balance: O(1)
    pre_order: (logn)


'''

class TreeNode(object):
    '''
        Author: Kyle Ong
        Date: 03/20/2018

        TreeNode Class

    '''
    def __init__(self,val):
        '''
            Author: Kyle Ong
            Date: 03/20/2018

            Type: val: int
        '''
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    '''
        Author:Kyle Ong
        Date: 03/20/2018

        AVL Tree implmentation
        - [ ] insert
        - [ ] left_rotate
        - [ ] right_rotate
        - [ ] get_height
        - [ ] get_balance
        - [ ] get_balance
        - [ ] pre_order


    '''
    
    def insert(self,root,val):
        '''
            Author: Kyle Ong
            Date: 03/20/2018

            Type: root: TreeNode
            Type: val: int

        '''
        if not root: return TreeNode(val)
        elif val < root.val: root.left = self.insert(root.left,val)
        else: root.right = self.insert(root.right,val)

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))

        load = self.get_balance(root)

        if load > 1 and val > root.left.val: #left - right case
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if load > 1 and val < root.left.val: #left - left case
            return self.right_rotate(root)
        if load < -1 and val > root.right.val: #right - right case
            return self.left_rotate(root)
        if load < -1 and val < root.right.val: #right - left case
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
    
        return root

    def left_rotate(self,x):
        '''
            Author: Kyle Ong
            Date: 03/21/2018

            left rotate for avl tree

            runtime: O(1)
            space: O(1)

            Type: x: TreeNode
            Type: Return TreeNode
        '''
        y = x.right
        sub_tree = y.left

        x.right = sub_tree
        y.left = x

        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


    def right_rotate(self,x):
        '''
            Author: Kyle Ong
            Date: 03/21/2018

            right rotate for avl tree

            runtime: O(1)
            space: O(1)

            Type: x: TreeNode
            Type: Return: TreeNode

        '''
        y = x.left
        sub_tree = y.left

        y.right = x
        x.left = sub_tree

        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return y


    def get_height(self,root):
        '''
            Author: Kyle Ong
            Date: 03/21/2018

            get_height for avl tree

            Type: root: TreeNode
            Type: Return: int

            runtime:O(logn)
            space:O(1)

        '''
        if not root: return 0
        return root.height
    
    def get_balance(self,root):
        '''
            Author: Kyle Ong
            Date: 03/21/2018

            get_balance for avl tree

            Type: root: TreeNode
            Type: balance: int

            runtime: O(logn)
            space: O(1)
        '''
        if not root: return 0
        balance = self.get_height(root.left) - self.get_height(root.right)
        return balance
        
    
    def pre_order(self,root):
        '''
            Author: Kyle Ong
            Date: 03/21/2018

            pre_order for avl tree

            runtime: O(logn)
            space: O(1)

            Type: root: TreeNode
            Type: Return: None
        '''
    
        if not root: return
        print("{0} ".format(root.val))
        self.pre_order(root.left)
        self.pre_order(root.right)


def main():
    print("it's alive")
    myTree = AVLTree()
    root = None
 
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)
 
    """The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
 
    # Preorder Traversal
    print("Preorder traversal of the",
      "constructed AVL tree is")
    myTree.pre_order(root)
    print()
    

main()