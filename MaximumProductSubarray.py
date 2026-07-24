class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprodarray = [0] * len(nums)
        maxprodarray = [0] * len(nums)
        minprodarray[0] = nums[0]
        maxprodarray[0] = nums[0]
        for i in range(1, len(nums)):
            maxprodarray[i] = max(maxprodarray[i - 1] * nums[i], nums[i], minprodarray[i - 1] * nums[i])
            minprodarray[i] = min(maxprodarray[i - 1] * nums[i], nums[i], minprodarray[i - 1] * nums[i])
        return max(maxprodarray)
