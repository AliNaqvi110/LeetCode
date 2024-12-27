class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmaps = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmaps:
                return [i, hashmaps[compliment]]
            hashmaps[nums[i]] = i
        return []

        