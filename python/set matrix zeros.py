class Solution(object):
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
            
        m = len(matrix)
        n = len(matrix[0])
        
        row_zero = False
        col_zero = False
        
        # Step 1: Check if first row has a zero
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break
                
        # Step 1: Check if first column has a zero
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
                
        # Step 2: Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 3: Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 4: Zero out the first row if needed
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # Step 4: Zero out the first column if needed
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
