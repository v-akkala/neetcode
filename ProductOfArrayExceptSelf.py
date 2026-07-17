class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0] * l
        suffix = [0] * l
        prefix[0] = nums[0]
        suffix[l - 1] = nums[l - 1]
        ans = []
        for i in range(1, l):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[l - 1 - i] = suffix[l - i] * nums[l - i - 1]
        for j in range(l):
            if j == 0:
                ans.append(suffix[1])
            elif j == l - 1:
                ans.append(prefix[l - 2])
            else:
                ans.append(prefix[j - 1] * suffix[j + 1])
        return ans
