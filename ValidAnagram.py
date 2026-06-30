class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        numletint = {}
        numletins = {}
        for c in s:
            numletins[c] = numletins.get(c, 0) + 1
        for c in t:
            numletint[c] = numletint.get(c, 0) + 1
        if(numletins == numletint):
            return True
        return False

