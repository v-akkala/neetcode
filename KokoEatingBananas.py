class Solution:
    def minEatingSpeed(self, piles, h):

        def isValid(val):
            th = 0
            for pile in piles:
                th += (pile + val - 1) // val
            if th <= h:
                return True
            return False

        low = 1
        high = max(piles)

        while low < high:
            mid = (high + low) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1
        return low

