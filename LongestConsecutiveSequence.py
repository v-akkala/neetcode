class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = {}
        longest = 0
        numset = set(nums)
        nums = list(numset)
        for i in range(len(nums)):
            consec[nums[i] + 1] = i
        for j in range(len(nums)):
            curlong = 1
            curidx = j
            if nums[curidx] in consec and nums[curidx] + 1 not in numset:
                while nums[curidx] in consec:
                    curlong += 1
                    curidx = consec[nums[curidx]]
            longest = max(curlong, longest)
        return longest
