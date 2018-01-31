""" Node is defined as

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    return checkBSTfunc(root,1,10000)

def checkBSTfunc(root,min_num,max_num):
    
    if root == None:
        return True
    
    if root.data > max_num or root.data < min_num:
        return False
    
    else:
        check1 = checkBSTfunc(root.left,min_num,root.data-1)
        check2 = checkBSTfunc(root.right,root.data+1,max_num)
        return (check1 and check2)
