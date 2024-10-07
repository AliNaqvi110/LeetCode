class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # get max candies
        greatest = max(candies)
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)
        return res
        