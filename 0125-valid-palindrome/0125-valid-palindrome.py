class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = ''
        for i in s.lower():
            if i.isalnum():
                sl +=i
        return True if sl==sl[::-1] else False
        