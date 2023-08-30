class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        max_num = max(hours)
        min_num = min(hours)
        if target > max_num:
            return 0
        elif (target < min_num):
            return len(hours)
        else:
            return sum([x >= target for x in hours])