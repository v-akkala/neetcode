class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        perm = []
        numslen = len(nums)

        def backtrack(perm, nums):
            if not nums:
                perms.append(perm)

            for i in range(len(nums)):
                num = nums.pop(i)
                backtrack(perm + [num], nums)
                nums.insert(i, num)

        backtrack(perm, nums)

        return perms




