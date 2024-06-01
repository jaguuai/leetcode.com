class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers at the ends of the list
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Iterate until the two pointers meet
        while left < right:
            # Calculate the area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(sol.maxArea([1, 1]))  # Output: 1
