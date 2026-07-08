class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = {}
        for num in nums:
            numfreq[num] = numfreq.get(num, 0) + 1
        ansheap = []
        for x in numfreq:
            heapq.heappush(ansheap, (numfreq[x], x))
            if len(ansheap) > k:
                heapq.heappop(ansheap)
        ans = []
        for x in range(k):
            _, num = heapq.heappop(ansheap)
            ans.append(num)
        return ans
