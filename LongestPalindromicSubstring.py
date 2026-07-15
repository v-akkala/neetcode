class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(0, len(s) - 1):
            exp = 1
            cur = 1
            while exp <= i and exp + i <= len(s) - 1:
                if s[i + exp] == s[i - exp]:
                    cur += 2
                else:
                    break
                exp += 1
            exp -= 1
            if len(s[i - exp: i + exp + 1]) > len(ans):
                ans = s[i - exp: i + exp + 1]
            cur = 0
            left = i
            right = i + 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    cur += 2
                else:
                    break
                left -= 1
                right += 1
            left += 1
            right -= 1
            if len(s[left:right+1]) > len(ans):
                ans = s[left:right+1]
        return ans
