class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.ans = False
        self.visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.backtrack(0, row, col)
                if self.ans:
                    return self.ans
        return self.ans
    
    def backtrack(self, letteridx, row, col):
        if (row, col) in self.visited:
            return
        if self.board[row][col] == self.word[letteridx]:
            letteridx += 1
        else:
            return
        self.visited.add((row, col))
        if letteridx == len(self.word):
            self.ans = True
            return
        if row < len(self.board) - 1:
            self.backtrack(letteridx, row + 1, col)
        if row > 0:
            self.backtrack(letteridx, row - 1, col)
        if col < len(self.board[0]) - 1:
            self.backtrack(letteridx, row, col + 1)
        if col > 0:
            self.backtrack(letteridx, row, col - 1)
        self.visited.remove((row, col))
