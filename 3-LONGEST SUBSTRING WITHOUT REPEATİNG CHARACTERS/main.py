"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
    
sol=Solution()
result=sol.lengthOfLongestSubstring("pwwkew")
print(result)
"""
Step by Step Example
Let's say the input string is "abcabcbb".

right = 0, s[right] = 'a': charSet = {a}, maxLength = 1
right = 1, s[right] = 'b': charSet = {a, b}, maxLength = 2
right = 2, s[right] = 'c': charSet = {a, b, c}, maxLength = 3
right = 3, s[right] = 'a': 'a' exists in the charSet, so left moves up to 1 and 'a' is removed from the charSet. Then s[right] = 'a' is added.
right = 4, s[right] = 'b': 'b' exists in the charSet, so left moves up to 2 and 'b' is removed from the charSet. Then s[right] = 'b' is added.
right = 5, s[right] = 'c': 'c' exists in the charSet, so left moves up to 3 and 'c' is removed from the charSet. Then s[right] = 'c' is added.
right = 6, s[right] = 'b': 'b' exists in the charSet, so left moves up to 5 and 'b' is removed from the charSet. Then s[right] = 'b' is added.
right = 7, s[right] = 'b': 'b' exists in the charSet, so left moves up to 6 and 'b' is removed from the charSet. Then s[right] = 'b' is added.
"""