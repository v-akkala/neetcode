class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            temp = []
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    temp.append(dp[j] + 1)
            if temp:
                dp[i] = max(temp)
        return max(dp)
