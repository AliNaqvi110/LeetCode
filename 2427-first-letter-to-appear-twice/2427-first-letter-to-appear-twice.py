class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = {}
        for i in s:
            if i in count:
               return i
            else:
                count[i] =1
        
        