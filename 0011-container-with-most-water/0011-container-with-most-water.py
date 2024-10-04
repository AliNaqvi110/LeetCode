class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right, maxwater = 0, len(height) - 1, 0
        while left < right:
            height_left = height[left]
            height_right = height[right]
            width = right - left
            area = min(height_left, height_right) * width 
            maxwater = max(maxwater, area)
            if height_left <= height_right:
                left +=1
            else:
                right -=1
        return maxwater