class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        comp = len(nums)//3
        counts = {}
        majority = []

        for element in nums:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1

        for key, value in counts.items():
            if value > comp:
                majority.append(key)
        # return list
        return majority