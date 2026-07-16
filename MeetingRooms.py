class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        timeline = []
        cur = 0
        for time in intervals:
            timeline.append((time[0], 1))
            timeline.append((time[1], -1))
        timeline.sort()
        for time, se in timeline:
            cur += se
            if cur > 1:
                return False
        return True
