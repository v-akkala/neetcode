class Solution:
    def subsets(self, nums):
        subsets = set()
        subset = []

        def backtrack(subset, nums):
            subsets.add(tuple(sorted(subset)))
            for i in range(len(nums)):
                num = nums.pop(i)
                backtrack(subset + [num], nums)
                nums.insert(i, num)

        backtrack(subset, nums)

        return [list(subset) for subset in subsets]
