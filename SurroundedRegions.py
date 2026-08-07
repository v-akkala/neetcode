class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if (row, col) in visited:
                return
            visited.add((row, col))
            coords.append((row, col))
            if row == 0 or row == len(board) - 1:
                self.turnx = False
            if col == 0 or col == len(board[0]) - 1:
                self.turnx = False
            if row > 0 and board[row - 1][col] == "O":
                dfs(row - 1, col)
            if row < len(board) - 1 and board[row + 1][col] == "O":
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == "O":
                dfs(row, col - 1)
            if col < len(board[0]) - 1 and board[row][col + 1] == "O":
                dfs(row, col + 1)

        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    coords = []
                    self.turnx = True
                    dfs(row, col)
                    if self.turnx:
                        for r, c in coords:
                            board[r][c] = "X"

