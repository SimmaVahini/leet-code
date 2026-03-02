class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        
        cur_row = 0
        going_down = False
        
       
        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1

        return "".join(rows)
