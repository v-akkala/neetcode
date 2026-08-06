class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        lastnum = -1
        for idx, num in enumerate(height):

            while stack and stack[-1][0] <= num:
                lastnum, lastidx = stack.pop()
                if not stack:
                    break
                ans += (min(stack[-1][0], num) - lastnum) * (idx - stack[-1][1] - 1)

            stack.append([num, idx])

        return ans

