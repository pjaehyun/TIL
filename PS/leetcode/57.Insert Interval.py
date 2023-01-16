class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        answer = []

        answer.append(intervals.pop(0))

        while intervals:
            x, y = intervals.pop(0)
            
            if x <= answer[-1][1] and y > answer[-1][1]:
                answer[-1][1] = y
            elif x > answer[-1][1]:
                answer.append([x,y])
        return answer