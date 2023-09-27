class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = ''
        for i in s.lower():
            if i.isalnum():
                sl +=i
        left  = 0
        right = len(sl) -1
        while(left < right):
            if sl[left] != sl[right]: return False
            left  +=1
            right -=1
        return True 
        