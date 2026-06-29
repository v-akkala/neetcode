class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setofnums = set(nums)
        if(len(nums) == len(setofnums)):
           return False
        return True
        
