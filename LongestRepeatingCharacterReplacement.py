class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        ans = 0
        chardict = {}
        while right < len(s):
            chardict[s[right]] = chardict.get(s[right], 0) + 1
            while (sum(1 for val in chardict.values() if val > k) <= 1 
            and sum(val for key, val in chardict.items() if key != max(chardict, key=chardict.get))) > k:
                ans = max(ans, right - left)
                chardict[s[left]] = chardict[s[left]] - 1
                left += 1
            while sum(1 for val in chardict.values() if val > k) >= 2:
                ans = max(ans, right - left)
                chardict[s[left]] = chardict[s[left]] - 1
                left += 1
            right += 1
        ans = max(ans, right - left)
        return ans
