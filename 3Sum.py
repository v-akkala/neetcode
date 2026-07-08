class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for x in range(0, len(nums) - 1):
            lidx = x + 1
            low = nums[lidx]
            hidx = len(nums) - 1
            high = nums[hidx]
            while hidx != lidx:
                if hidx != lidx:
                    if nums[x] + low + high == 0:
                        ans.append([nums[x], low, high])
                if abs(low) > abs(high):
                    lidx += 1
                    low = nums[lidx]
                else:
                    hidx -= 1
                    high = nums[hidx]
        return ans
