class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        end = 0
        nz = 0
        ans = 0
        while end < len(nums):
            if nums[end] == 0:
                nz += 1
            while nz > k:
                if nums[start] == 0:
                    nz -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans
