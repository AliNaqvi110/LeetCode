class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1     
            else:
                count[i] += 1
        for i in count:
            if count[i] == 1:
                return s.index(i)
        return -1

        