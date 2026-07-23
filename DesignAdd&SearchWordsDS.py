class Char:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = Char()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Char()
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        i = 0
        return self.recursedots(word, i, cur)

    def recursedots(self, word, index, node):
        if index == len(word):
            return node.endofword
        if word[index] == ".":
            for children in node.children.values():
                if self.recursedots(word, index + 1, children):
                    return True
            return False
        else:
            if word[index] in node.children:
                return self.recursedots(word, index + 1, node.children[word[index]])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
