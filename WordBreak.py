class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordbreaks = [False] * len(s) + 1
        wordbreaks[0] = True
        maxlen = 0
        for word in wordbreaks:
            maxlen = max(maxlen, len(word))
        for i in range(1, len(s)):
            for j in range(i, max(-1, i - maxlen), -1)
                if wordbreaks[j] = True:
                    curword = s[j + 1:i + 1]
                    if curword in wordDict:
                        wordbreaks[i] = True
                        break
        return wordbreaks[len(s)]

