class Solution:
    def reverse(self, x: int) -> int:
        # Define the limits for a 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Initialize the result as 0
        result = 0
        
        # Save the original sign of x
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        while x != 0:
            # Pop the last digit from x
            digit = x % 10
            x //= 10
            
            # Check if the result will overflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            
            # Push the digit to the result
            result = result * 10 + digit
        
        return sign * result

# Example Usage:
sol = Solution()
print(sol.reverse(123))    # Output: 321
print(sol.reverse(-123))   # Output: -321
print(sol.reverse(120))    # Output: 21
print(sol.reverse(0))      # Output: 0
print(sol.reverse(1534236469)) # Output: 0 (overflow case

"""
More useful code:
class Solution:
    def reverse(self, x: int) -> int:
        MIN = - 2**31

        ret = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x > 0:
            x, mod = divmod(x, 10)
            ret = ret * 10 + mod
        ret *= sign
        
        return ret if MIN <= ret <= -MIN-1 else 0
"""