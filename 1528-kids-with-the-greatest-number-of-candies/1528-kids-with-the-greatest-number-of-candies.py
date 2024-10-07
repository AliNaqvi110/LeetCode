class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # get max candies
        threshold = max(candies) - extraCandies

        res = [candies[i] >= threshold for i in range(len(candies))]
        return res
        