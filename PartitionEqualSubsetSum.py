class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsum = sum(nums)
        if numsum % 2 != 0:
            return False

        target = numsum // 2
        dp = [([None] * (target + 1)) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp[0])):
            dp[0][i] = False

        def dyp(i, j):
            if i == 0:
                return dp[0][j]
            if dp[i][j]:
                return True
            elif dp[i][j] == False:
                return False
            else:
                if j - nums[i - 1] < 0:
                    dp[i][j] = dyp(i - 1,j)
                else:
                    dp[i][j] = dyp(i - 1,j) or dyp(i - 1,j - nums[i - 1])
            return dp[i][j]

        dyp(len(nums), target)

        return dp[len(nums)][target]
