class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        cur_row = 0
        direction = -1
        
        for char in s:
            rows[cur_row] += char
            
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            
            cur_row += direction
        
        return "".join(rows)
