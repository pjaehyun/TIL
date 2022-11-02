class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                result += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return result
