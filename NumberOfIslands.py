class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in self.visited:
                    self.dfs(row, col, grid)
                    self.ans += 1
        return self.ans
        
    def dfs(self, row: int, col: int, grid: List[List[str]]):
        if (row, col) in self.visited:
            return
        elif row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
            return
        elif grid[row][col] != "1":
            return
        else:
            self.visited.add((row, col))
        self.dfs(row + 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col - 1, grid)
