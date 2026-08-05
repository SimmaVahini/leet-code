# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        memo = {}
        
        def buildTrees(start, end):
            # Base case: if start > end, there are no elements to form a tree.
            # Return a list containing None (representing an empty subtree).
            if start > end:
                return [None]
                
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            
            # Pick a root node i
            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = buildTrees(start, i - 1)
                right_trees = buildTrees(i + 1, end)
                
                # Connect left and right subtrees to the root i
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees
            
        return buildTrees(1, n)
