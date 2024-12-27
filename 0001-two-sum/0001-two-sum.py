class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in my_dict:
                return [i, my_dict[compliment]]
            my_dict[nums[i]] = i
        return []