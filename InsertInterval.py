class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0] or intervals[i+1][1] < intervals[i][1]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                ans.append([intervals[i][0], intervals[i][1]])
            i += 1
        ans.append([intervals[i][0], intervals[i][1]])
        return ans
