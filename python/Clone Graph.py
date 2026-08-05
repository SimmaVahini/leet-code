"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
            
        # Dictionary to map original nodes to their cloned counterparts
        cloned = {}
        
        def dfs(curr_node):
            # If the node is already cloned, return the cloned instance
            if curr_node in cloned:
                return cloned[curr_node]
                
            # Create a deep copy of the current node
            copy = Node(curr_node.val)
            cloned[curr_node] = copy
            
            # Recursively clone and add all neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)
