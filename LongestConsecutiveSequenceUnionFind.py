class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = {}
        longest = 0
        visited = set()
        v = False
        for i in range(len(nums)):
            consec[nums[i] + 1] = i
        for j in range(len(nums)):
            curlong = 1
            curidx = j
            while nums[curidx] in consec:
                if curidx in visited:
                    v = True
                    curidx = consec[nums[curidx]]
                    curlong += consec[nums[curidx]] - 1
                    break
                visited.add(curidx)
                curlong += 1
                temp = consec[nums[curidx]]
                consec[nums[curidx]] = j
                curidx = temp
            if not v:
                consec[nums[j]] = curlong
            v = False
            longest = max(curlong, longest)
        return longest
