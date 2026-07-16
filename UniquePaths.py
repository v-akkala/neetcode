class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if i == 0:
                    memo[i][j] = memo[i][j-1]
                elif j == 0:
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[m-1][n-1]
