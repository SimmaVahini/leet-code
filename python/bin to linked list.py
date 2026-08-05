# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Wire the rightmost node's right to current's right child
                rightmost.right = curr.right
                
                # Move the entire left subtree to the right side
                curr.right = curr.left
                curr.left = None
                
            # Move on to the next node on the right
            curr = curr.right
