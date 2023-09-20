class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            res = digits[i] + carry
            carry = res // 10
            digits[i] = res % 10

        if carry > 0:
            carry_digits = [int(digit) for digit in str(carry)]
            digits = carry_digits + digits

        return digits

