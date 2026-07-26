class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timeline = []
        for interval in intervals:
            timeline.append((interval[0], 1))
            timeline.append((interval[1], -1))
        timeline.sort()
        ans = 0
        cur = 0
        maxrooms = 0
        for time in timeline:
            cur += time[1]
            maxrooms = max(maxrooms, cur)
        return maxrooms
