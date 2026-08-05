# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(node, current_sum, current_path):
            if not node:
                return
                
            # Include the current node's value in our path tracking
            current_path.append(node.val)
            
            # Check if it's a leaf node and if the path sum matches targetSum
            if not node.left and not node.right:
                if current_sum == node.val:
                    res.append(list(current_path))
            else:
                # Continue exploring left and right subtrees
                backtrack(node.left, current_sum - node.val, current_path)
                backtrack(node.right, current_sum - node.val, current_path)
                
            # Backtrack: Remove the current node's value before returning up the stack
            current_path.pop()
            
        backtrack(root, targetSum, [])
        return res
