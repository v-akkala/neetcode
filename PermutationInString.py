class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hash = defaultdict(int)

        for char in s1:
            s1hash[char] += 1

        if len(s1) > len(s2):
            return False

        start = 0
        end = len(s1)

        s2hash = defaultdict(int)

        for i in range(end):
            s2hash[s2[i]] += 1

        if s1hash == s2hash:
            return True

        while end < len(s2):
            delchar = s2[start]
            s2hash[delchar] -= 1
            if s2hash[delchar] == 0:
                s2hash.pop(delchar)
            addedchar = s2[end]
            s2hash[addedchar] += 1
            if s1hash == s2hash:
                return True
            start += 1
            end += 1
        return False
