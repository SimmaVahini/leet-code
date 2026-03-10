class Solution(object):
    def exist(self, board, word):
       
        ROWS = len(board)
        COLS = len(board[0])
        
        def backtrack(r, c, index):
           
            if index == len(word):
                return True
            
            
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[index]):
                return False
            
           
            temp = board[r][c]
            board[r][c] = "#"
            
           
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
        
            board[r][c] = temp
            return found

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False
