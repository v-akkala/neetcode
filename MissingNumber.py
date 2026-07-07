class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(0, len(nums)):
            if nums[x] ^ x != 0:
                return x
        return len(nums)
