class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        sort_strs = sorted(strs)
        first = sort_strs[0]
        last = sort_strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return result
            result +=first[i]
        return result