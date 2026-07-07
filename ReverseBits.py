class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for x in range(0, 32):
            if n % 2 == 1:
                n = n >> 1
                ans = ans << 1
                ans += 1
            else:
                n = n >> 1
                ans = ans << 1
        return ans
