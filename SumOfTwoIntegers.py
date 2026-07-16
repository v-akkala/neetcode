class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        neg = False
        if a <= 0 and b <= 0:
            neg = True
            a = (~a) + 1
            b = (~b) + 1
        abit = a
        bbit = b
        for x in range(11):
            switch = (abit & 1) + (bbit & 1) + (carry)
            if switch == 3:
                carry = 1
                ans |= 1 << x
            elif switch == 2:
                carry = 1
            elif switch == 1:
                carry = 0
                ans |= 1 << x
            else:
                carry = 0
            abit = abit >> 1
            bbit = bbit >> 1
        if (a < 0 and b > 0 and abs(a) > abs(b)) or (a > 0 and b < 0 and abs(a) < abs(b)):
            return ~(2048 - ans) + 1
        if neg:
            return (~ans) + 1
        return ans
