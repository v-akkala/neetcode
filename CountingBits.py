class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for x in range(0, n + 1):
            ones = 0
            while x > 0:
                if x % 2 == 1:
                    ones += 1
                    x = x >> 1
                else:
                    x = x >> 1
            ans.append(ones)
        return ans
