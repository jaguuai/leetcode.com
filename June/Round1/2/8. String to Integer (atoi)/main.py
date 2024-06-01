class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespace
        s = s.strip()
        
        # Step 2: Determine the sign
        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        # Step 3: Convert digits
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Step 4: Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result *= sign
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result

# Example Usage:
sol = Solution()
print(sol.myAtoi("42"))        # Output: 42
print(sol.myAtoi(" -042"))     # Output: -42
print(sol.myAtoi("1337c0d3"))  # Output: 1337
print(sol.myAtoi("0-1"))       # Output: 0
print(sol.myAtoi("words and 987"))  # Output: 0
