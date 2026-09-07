class Solution:
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost) + 2)
        cost.append(0)
        dp[1] = cost[0]
        dp[2] = cost[1]
        if len(cost) == 2:
            return min(cost)
        for i in range(3, len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]
        return dp[-1]
