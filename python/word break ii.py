class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Convert list to a set for constant time O(1) lookups
        word_set = set(wordDict)
        memo = {}
        
        def dfs(remaining_str):
            # Base case: if remaining string is empty, return a list containing an empty string
            if not remaining_str:
                return [""]
                
            # Return cached result if already calculated
            if remaining_str in memo:
                return memo[remaining_str]
                
            sentences = []
            
            # Try every possible prefix length
            for i in range(1, len(remaining_str) + 1):
                prefix = remaining_str[:i]
                
                if prefix in word_set:
                    suffix = remaining_str[i:]
                    # Recursively solve for the remaining suffix
                    sub_sentences = dfs(suffix)
                    
                    # Combine the current prefix with all valid suffix sentences
                    for sub in sub_sentences:
                        if sub:
                            sentences.append(prefix + " " + sub)
                        else:
                            sentences.append(prefix)
                            
            memo[remaining_str] = sentences
            return sentences
            
        return dfs(s)
