from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
            
        # Adjacency list to track valid parent -> child paths
        adj = defaultdict(list)
        curr_level = set([beginWord])
        found = False
        
        # Step 1: BFS to find layers and build the graph structure
        while curr_level and not found:
            # Safely remove all words visited in the previous levels
            word_set -= curr_level
            next_level = set()
            
            for word in curr_level:
                for i in range(len(word)):
                    original_char = word[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in word_set:
                            if next_word == endWord:
                                found = True
                            next_level.add(next_word)
                            adj[word].append(next_word)
            curr_level = next_level
            
        # Step 2: DFS to collect all valid paths from the graph
        res = []
        if not found:
            return res
            
        def dfs(word, path):
            if word == endWord:
                res.append(list(path))
                return
            for next_word in adj[word]:
                path.append(next_word)
                dfs(next_word, path)
                path.pop()
                
        dfs(beginWord, [beginWord])
        return res
