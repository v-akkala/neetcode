class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        ans = min(height[start], height[end]) * (end - start)
        while start != end:
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                if start - 1 == end:
                    ans = max((min(height[start], height[end]) * (end - start)), ans)
                    break
                else:
                    start += 1
                    end -= 1
            ans = max((min(height[start], height[end]) * (end - start)), ans)
        return ans
