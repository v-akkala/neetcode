class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tlet = {}
        for c in t:
            tlet[c] = tlet.get(c, 0) + 1
        start = 0
        end = 0
        bests = ""
        cur = {}
        while end != len(s):
            if s[end] in tlet:
                cur[s[end]] = cur.get(s[end], 0) + 1
            while self.hassub(cur, tlet):
                if end - start + 1 < len(bests) or bests == "":
                    bests = s[start:end+1]
                if s[start] in cur:
                    cur[s[start]] -= 1
                start += 1
            end += 1
        return bests
    
    def hassub(self, cur, tlets):
        if cur.keys() != tlets.keys():
            return False
        for k in cur:
            if cur[k] < tlets[k]:
                return False
        return True
