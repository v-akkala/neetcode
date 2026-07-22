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
        while i < len(word):
            if word[i] != ".":
                if word[i] in cur.children:
                    cur = cur.children[word[i]]
                else:
                    return False
            else:
                c = 0
                while word[i + c] == ".":
                    c += 1
                    if i + c >= len(word) - 1: 
                        return True
                for node in cur.children.values():
                    if word[i + 1] in node.children:
                        cur = node.children[word[i + 1]]
                        i += 1
                        break
                    else:
                        return False
            i += 1
        return cur.endofword


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
