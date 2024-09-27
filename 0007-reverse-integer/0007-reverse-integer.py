class Solution:
    def reverse(self, x: int) -> int:
        minbit = -2**31         # Signed integer lower range
        maxbit = 2**31 - 1      # signed integer upper range
        is_negative = False
        if x < 0:
            is_negative = True     # track if x is negative
            x *=-1
        
        res = 0   
        while x > 0:
            res = (res*10) + (x%10)    
            x //= 10
        if is_negative:   # apply negative sign if it was
            res =res * -1

        if minbit <= res <= maxbit:     # make sure a 32 bit signed integer
            return res
        else:
            return 0
        