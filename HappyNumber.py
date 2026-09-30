class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while cur not in seen:
            seen.add(cur)
            nextnum = 0
            cur = str(cur)
            for digit in cur:
                nextnum += int(digit) * int(digit)
            cur = nextnum
            if cur == 1:
                return True
        return False
