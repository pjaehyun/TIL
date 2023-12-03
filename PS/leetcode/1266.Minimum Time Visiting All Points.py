class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0

        for i in range(1, len(points)):
            x = abs(points[i-1][0] - points[i][0])
            y = abs(points[i-1][1] - points[i][1])

            answer += min(x, y)
            answer += abs(x-y)
        return answer