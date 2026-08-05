from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Convert list to set for O(1) lookups
        word_set = set(wordList)
        
        # If endWord is not in the dictionary, no valid sequence can exist
        if endWord not in word_set:
            return 0
            
        # Queue stores pairs of (current_word, sequence_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, level = queue.popleft()
            
            # If we reached the target word, return the length
            if current_word == endWord:
                return level
                
            # Try changing each character of the word
            for i in range(len(current_word)):
                original_char = current_word[i]
                
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                        
                    # Form the new word variant
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If variant is valid, add to queue and remove from set to mark as visited
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, level + 1))
                        
        return 0
