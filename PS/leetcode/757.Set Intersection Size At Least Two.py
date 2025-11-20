class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        p1 = intervals[0][1]-1
        p2 = intervals[0][1]
        answer = 2


        for i in range(1, len(intervals)):
            if p2 < intervals[i][0]:
                p1 = intervals[i][1]-1
                p2 = intervals[i][1]
                answer += 2
            elif p1 < intervals[i][0]:
                if intervals[i][1] == p2:
                    p1 = intervals[i][1]-1
                else:
                    p1 = intervals[i][1]
                p1, p2 = min(p1, p2), max(p1, p2)
                answer += 1
        return answer