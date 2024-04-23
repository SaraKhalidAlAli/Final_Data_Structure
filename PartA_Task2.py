#TASK 2

#defining the class of the tree
class TreeNode:
    def __init__(self, datetime, post, left=None, right=None): #initializing
        self.datetime = datetime
        self.post = post
        self.left = left
        self.right = right