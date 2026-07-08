class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            tempdict = {}
            for c in s:
                tempdict[c] = tempdict.get(c, 0) + 1
            anagrams.setdefault(frozenset(tempdict.items()), []).append(s)
        ans = []
        for val in anagrams.values():
            ans.append(key)
        return ans
