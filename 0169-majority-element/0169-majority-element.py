class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        comp = len(nums)/2
        counts = {}
        for element in nums:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1
                
        for key, value in counts.items():
            if value > comp:
                return key
        