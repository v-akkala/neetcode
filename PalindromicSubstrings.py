class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s) - 1):
            ans += 1
            exp = 1
            while exp <= i and exp + i <= len(s) - 1:
                if s[i + exp] == s[i - exp]:
                    ans += 1
                else:
                    break
                exp += 1
            left = i
            right = i + 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    ans += 1
                else:
                    break
                left -= 1
                right += 1
        ans += 1
        return ans
