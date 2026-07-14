class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 3:
            return max(nums)
        temp = nums.pop()
        memo = [0] * (len(nums))
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])
        for x in range(2, len(nums)):
            memo[x] = max(memo[x-1], memo[x-2] + nums[x])
        nums = nums[1:]
        nums.append(temp)
        memo2 = [0] * (len(nums))
        memo2[0] = nums[0]
        memo2[1] = max(nums[0], nums[1])
        for x in range(2, len(nums)):
            memo2[x] = max(memo2[x-1], memo2[x-2] + nums[x])
        return max(max(memo), max(memo2))
