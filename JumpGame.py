class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curjump = nums[0]
        i = 0
        while i < len(nums) - 1:
            if curjump == 0:
                return False
            i += 1
            curjump = max(curjump - 1, nums[i])
        return True
