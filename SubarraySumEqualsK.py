class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        sumdict = defaultdict(list)
        sumdict[0] = [0]
        ans = 0
        for i, num in enumerate(nums):
            cur += num
            target = cur - k
            if target in sumdict:
                ans += len(sumdict[target])
            sumdict[cur].append(i)
        return ans
