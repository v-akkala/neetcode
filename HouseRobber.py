class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = [0] * len(nums)
        self.dp(nums)
        print(self.memo)
        return max(self.memo)

    def dp(self, nums: List[int]):
        if len(nums) == 1:
            self.memo[0] = nums[0]
            return
        self.memo[0], self.memo[1] = nums[0], nums[1]
        if len(nums) == 2:
            return
        self.memo[2] = self.memo[0] + nums[2]
        if len(nums) == 3:
            return
        for x in range(3, len(nums)):
            print(self.memo[x - 2] + self.memo[x - 4], self.memo[x - 3])
            self.memo[x] = nums[x] + max(self.memo[x - 2], self.memo[x - 3])

