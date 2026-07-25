class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordbreaks = [False] * (len(s) + 1)
        wordbreaks[0] = True
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
        for i in range(1, len(s) + 1):
            for j in range(max(0, i-maxlen), i):
                if wordbreaks[j] == True:
                    curword = s[j:i]
                    if curword in wordDict:
                        wordbreaks[i] = True
        return wordbreaks[len(s)]

