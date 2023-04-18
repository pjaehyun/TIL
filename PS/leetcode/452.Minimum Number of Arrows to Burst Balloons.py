class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        curr = points.pop(0)
        answer = 1
        while points:
            next = points.pop(0)
            if curr[0] <= next[0] <= curr[1]:
                if curr[1] >= next[1]:
                    curr[1] = next[1]
                continue
            else:
                curr = next
                answer += 1
        return answer