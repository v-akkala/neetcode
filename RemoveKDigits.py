class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        for i in range(len(num)):
            while ans and ans[-1] > num[i] and k > 0:
                ans.pop()
                k -= 1
            ans.append(num[i])

        while ans and k > 0:
            ans.pop()
            k -= 1

        p = 0
        while p < len(ans) and ans[p] == "0":
            p += 1
        ans = "".join(ans)
        ans = ans[p:]
        if not ans:
            return "0"
        return ans
