class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        third = len(nums) - 1
        second = first + third // 2
        if len(nums) == 1:
            return nums[first]
        while first != third:
            if nums[third] < nums[third - 1]:
                return nums[third]
            if nums[second] < nums[second - 1]:
                return nums[second]
            if nums[first] < nums[first - 1]:
                return nums[first]
            if nums[first] <= nums[second] and nums[second] <= nums[third]:
                return nums[first]
            if nums[first] >= nums[second] and nums[second] <= nums[third]:
                third = second
                second = (first + third) // 2
                first += 1
            else:
                first = second
                second = (first + third) // 2
                third -= 1
        return nums[first]
