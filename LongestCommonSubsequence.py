class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [([0] * len(text2)) for _ in range(len(text1))]
        hit1 = False
        hit2 = False
        if text1[0] == text2[0]:
            dp[0][0] = 1
            hit1, hit2 = True, True
        for i in range(1, len(text1)):
            if text1[i] == text2[0] and not hit1:
                dp[i][0] = dp[i - 1][0] + 1
                hit1 = True
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, len(text2)):
            if text2[j] == text1[0] and not hit2:
                dp[0][j] = dp[0][j - 1] + 1 
                hit2 = True
            else:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1) - 1][len(text2) - 1]
