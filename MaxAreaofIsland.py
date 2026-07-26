class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()

        def dfs(row, col):
            if grid[row][col] == 0:
                return
            if (row, col) in visited:
                return
            self.cursum += 1
            visited.add((row, col))
            if row > 0:
                dfs(row - 1, col)
            if row < len(grid) - 1:
                dfs(row + 1, col)
            if col > 0:
                dfs(row, col - 1)
            if col < len(grid[0]) - 1:
                dfs(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.cursum = 0
                    dfs(row, col)
                    ans = max(ans, self.cursum)
        return ans
