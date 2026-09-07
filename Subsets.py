class Solution:
    def subsets(self, nums):
        ans = []

        def backtrack(cur, nums, start):
            ans.append(cur)
            for i in range(start, len(nums)):
                backtrack(cur + [nums[i]], nums, i + 1)

        backtrack([], nums, 0)

        return ans
