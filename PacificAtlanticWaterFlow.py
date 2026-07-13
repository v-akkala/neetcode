class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ans = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                self.visited = set()
                self.pacific = False
                self.atlantic = False
                self.isPA(row, col, heights)
                if self.atlantic and self.pacific:
                    self.ans.append([row, col])
        return self.ans


    def isPA(self, row: int, col: int, heights: List[List[int]]):
        cur = heights[row][col]
        if row == 0 or col == 0:
            self.pacific = True
        if row == len(heights) - 1 or col == len(heights[0]) - 1:
            self.atlantic = True
        if self.atlantic and self.pacific:
            return
        if (row, col) not in self.visited:
            self.visited.add((row, col))
            if row - 1 >= 0:
                if heights[row - 1][col] <= cur:
                    self.isPA(row - 1, col, heights)
            if row + 1 <= len(heights) - 1:
                if heights[row + 1][col] <= cur:
                    self.isPA(row + 1, col, heights)
            if col - 1 >= 0:
                if heights[row][col - 1] <= cur:
                    self.isPA(row, col - 1, heights)
            if col + 1 <= len(heights[0]) - 1:
                if heights[row][col + 1] <= cur:
                    self.isPA(row, col + 1, heights)
