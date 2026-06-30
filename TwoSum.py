class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        for i, v in enumerate(nums):
            if (target - v) in numhash:
                return [numhash[target-v], target-v]

