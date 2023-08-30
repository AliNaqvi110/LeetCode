class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        max_num = max(hours)
        if target > max_num:
            return 0
        else:
            return sum([x >= target for x in hours])