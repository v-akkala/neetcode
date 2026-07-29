class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsum = sum(nums)
        if numsum % 2 != 0:
            return False
        target = numsum / 2
        self.ans = False
        self.backtrack(nums, 0, 0, target)
        return self.ans

    def backtrack(self, nums, cursum, index, target):
        if cursum == target:
            self.ans = True
        elif cursum > target:
            return
        for i in range(index, len(nums)):
            self.backtrack(nums, cursum + nums[i], i + 1, target)
