class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Initialize the prefix to the first string
        prefix = strs[0]

        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Find the common prefix between the current prefix and the string s
            while s[:len(prefix)] != prefix and prefix:
                # Reduce the prefix by one character until a common prefix is found
                prefix = prefix[:-1]
            # If the prefix becomes empty, there is no common prefix
            if not prefix:
                break

        return prefix

# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
