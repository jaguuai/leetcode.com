class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a dictionary for memoization
        memo = {}

        def dp(i, j):
            # Check for memoized results
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we reach the end of the pattern
            if j == len(p):
                return i == len(s)
            
            # Current match check
            current_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If there's a '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Either treat '*' as zero occurrences or use '*' to match a character
                result = (dp(i, j + 2) or (current_match and dp(i + 1, j)))
            else:
                # Normal match
                result = current_match and dp(i + 1, j + 1)
            
            # Memoize and return the result
            memo[(i, j)] = result
            return result

        return dp(0, 0)

# Example Usage:
sol = Solution()
print(sol.isMatch("aa", "a"))     # Output: False
print(sol.isMatch("aa", "a*"))    # Output: True
print(sol.isMatch("ab", ".*"))    # Output: True
