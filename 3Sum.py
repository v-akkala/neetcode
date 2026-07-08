class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for x in range(0, len(nums) - 1):
            lidx = x + 1
            low = nums[lidx]
            hidx = len(nums) - 1
            high = nums[hidx]
            while hidx != lidx:
                if nums[x] + low + high == 0:
                    ans.add((nums[x], low, high))
                if nums[x] <= 0:
                    if low + high < -1 * nums[x]:
                        lidx += 1
                        low = nums[lidx]
                    else:
                        hidx -= 1
                        high = nums[hidx]
                else:
                    if low + high > -1 * nums[x]:
                        lidx += 1
                        low = nums[lidx]
                    else:
                        hidx -= 1
                        high = nums[hidx]
        return list(ans)
