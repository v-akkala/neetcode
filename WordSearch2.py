class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = ""

class Trie:
    def __init__(self, board):
        self.root = TrieNode()
        self.visited = set()
        self.board = board
        self.ans = set()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = word
    
    def search(self, row, col, node):
        cur = node
        if (row, col) in self.visited:
            return
        if self.board[row][col] in node.children:
            self.visited.add((row, col))
            cur = node.children[self.board[row][col]]
            if row > 0:
                self.search(row - 1, col, cur)
            if row < len(self.board) - 1:
                self.search(row + 1, col, cur)
            if col > 0:
                self.search(row, col - 1, cur)
            if col < len(self.board[0]) - 1:
                self.search(row, col + 1, cur)
        else:
            return
        self.visited.remove((row, col))
        if cur.endofword:
            self.ans.add(cur.endofword)
            return

    def returnAns(self):
        return self.ans

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordfinder = Trie(board)
        for word in words:
            wordfinder.addWord(word)
        for row in range(len(board)):
            for col in range(len(board[0])):
                wordfinder.search(row, col, wordfinder.root)
        return list(wordfinder.returnAns())

        
