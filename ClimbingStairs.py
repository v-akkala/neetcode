class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [0] * n
        return self.Climber(n)
        
    def Climber(self, n: int) -> int:
        if n == 1:
            return 1
        self.memo[0], self.memo[1] = 1, 2
        if n == 0:
            return 0
        if self.memo[n-1] > 0:
            return self.memo[n-1]
        self.memo[n-1] = self.Climber(n - 1) + self.Climber(n - 2)
        return self.memo[n-1]
