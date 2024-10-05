class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = maxlength = 0
        seen = set()
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end +=1
                maxlength = max(maxlength, end-start)
            else:
                seen.remove(s[start])
                start +=1
        return maxlength
                
        