class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] stores the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node tree
        
        # Fill the DP table
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_subtrees = dp[root - 1]
                right_subtrees = dp[nodes - root]
                dp[nodes] += left_subtrees * right_subtrees
                
        return dp[n]
