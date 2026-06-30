class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        for i, v in enumerate(nums):
            if v in numhash:
                return [numhash[v], i]
            numhash[target-v] = i
        


