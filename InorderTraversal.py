# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorderTraversalUtil(root, res): 
    if root is not None:
        if root.left is not None:
            inorderTraversalUtil(root.left, res)
        res.append(root.val)
        if root.right is not None:
            inorderTraversalUtil(root.right, res)
class Solution(object):
            
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        inorderTraversalUtil(root, res)
        return res
    
    
        
