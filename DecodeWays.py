class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * (len(s) + 1)
        memo[0] = 1
        if s[0] == "0":
            return 0
        memo[1] = 1
        for i in range(2, len(s) + 1):
            if int(s[i - 1]) == 0 and not (int(s[i - 2]) == 1 or int(s[i - 2]) == 2):
                return 0
            elif int(s[i - 1]) == 0 and (int(s[i - 2]) == 1 or int(s[i - 2]) == 2) and (int(s[i - 4]) > 2 or int(s[i-3]) == 0) and i < 3:
                memo[i] = memo[i - 1]
            elif int(s[i - 1]) == 0 and (int(s[i - 2]) == 1 or int(s[i - 2]) == 2):
                memo[i] = memo[i - 2]
            elif int(s[i - 2]) > 2 or int(s[i-2]) == 0:
                memo[i] = memo[i - 1]
            elif int(s[i - 2]) == 2 and int(s[i - 1]) > 6:
                memo[i] = memo[i - 1]
            else:
                memo[i] = memo[i - 1] + memo[i - 2]
        return memo[len(s)]
