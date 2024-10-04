class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxwater = 0, len(height) - 1, 0
        while left < right:
            area = (right-left) * min(height[left], height[right]) 
            maxwater = max(maxwater, area)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return maxwater