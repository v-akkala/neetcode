class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        index = 0
        start = s[index]
        end = s[index]
        curset = set()
        max = 0
        curmax = 0
        while index < len(s):
            curset.add(end)
            if s[index] not in curset:
                curset.add(s[index])
                curmax += 1
            else:
                start = s[index - (curmax - 1)]
                end = s[index - (curmax - 1)]
                if max < curmax:
                    max = curmax
                curmax = 1
                curset = set()
            index += 1
        if max < curmax:
            max = curmax
        return max
