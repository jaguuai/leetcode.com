"""""
Given a string s, return the longest 
palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str

sol=Solution()
result=sol.longestPalindrome("babad")
print(result)
"""
s = "babad"

1-i = 0, j = 1:
Substring: "ba"
Not a palindrome.

2-i = 0, j = 2:
Substring: "bab"
Palindrome.
Update Max_Len = 3 and Max_Str = "bab".

3-i = 0, j = 3:
Substring: "baba"
Not a palindrome.

4-i = 0, j = 4:
Substring: "babad"
Not a palindrome.

5-i = 1, j = 2:
Substring: "ab"
Not a palindrome.

6-i = 1, j = 3:
Substring: "aba"
Not a palindrome.

7-i = 1, j = 4:
Substring: "abad"
Not a palindrome.

8-i = 2, j = 3:
Substring: "ba"
Not a palindrome.

9-i = 2, j = 4:
Substring: "bad"
Not a palindrome.

10-i = 3, j = 4:
Substring: "ad"
Not a palindrome.
Step 3: Result

Since Max_Str = "bab", this value is returned.
"""
