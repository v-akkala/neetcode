class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        if len(nums) == 1:
            return nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            ans = max(cursum, ans)
        return ans

