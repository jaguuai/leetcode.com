class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there is only one row or the string is too short, return it directly
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list with numRows empty rows
        rows = [''] * numRows
        index = 0
        step = 1
        
        # Iterate over all characters
        for char in s:
            rows[index] += char
            
            # Update the index and direction
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            
            index += step
        
        # Join all rows and return the result
        return ''.join(rows)

# Example Usage:
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # "PINALSIGYAHRPI"
print(sol.convert("A", 1))  # "A"
