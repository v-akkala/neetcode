class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in numset:
            curlong = 0
            curnum = num
            if curnum in numset and curnum + 1 not in numset:
                while curnum in numset:
                    curlong += 1
                    curnum -= 1
            longest = max(curlong, longest)
        return longest
