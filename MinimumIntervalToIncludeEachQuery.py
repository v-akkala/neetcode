class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1] * len(queries)
        queryidxs = defaultdict(list)

        for j in range(len(queries)):
            queryidxs[queries[j]].append(j)

        queries.sort()
        intervals.sort()
        for interval in intervals:
            interval.append(interval[1] + 1 - interval[0])
        iheap = []
        i = 0
        for j in range(len(queries)):
            while iheap and (iheap[0][1][0] > queries[j] or iheap[0][1][1] < queries[j]):
                heapq.heappop(iheap)
            if iheap:
                for idx in queryidxs[queries[j]]:
                    ans[idx] = iheap[0][0]
            if i == len(intervals):
                continue

            while queries[j] > intervals[i][1]:
                i += 1
                if i == len(intervals):
                    break

            while i != len(intervals) and queries[j] >= intervals[i][0]:
                if queries[j] >= intervals[i][0] and queries[j] <= intervals[i][1]:
                    heapq.heappush(iheap, (intervals[i][2], intervals[i]))
                for idx in queryidxs[queries[j]]:
                    ans[idx] = iheap[0][0]
                i += 1
                if i == len(intervals):
                    break
        return ans
