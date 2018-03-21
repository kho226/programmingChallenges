'''
    Author: Kyle Ong
    Date: 03/20/2018

    avl tree

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


def insert(root,val):
    '''
        Author: Kyle Ong
        Date: 03/20/2018

        Type: root: TreeNode
        Type: val: int

    '''
    if not root: return TreeNode(val)
    if key < root.val: root.left = insert(root.left)
    else: root.right = insert(root.right)

    root.height = 1 + max(get_height(root.left),get_height(root.right))

    load = get_load(root.left,root.right)

    if load > 1 and val > root.left.val: #left - right case
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if load > 1 and val < root.left.val: #left - left case
        return right_rotate(root)
    if load < -1 and val > root.right.val: #right - right case
        return left_rotate(root)
    if load < -1 and val < root.right.val: #right - left case
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root