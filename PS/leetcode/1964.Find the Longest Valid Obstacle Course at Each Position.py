class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lst = []
        answer = []

        for n in obstacles:
            idx = bisect.bisect_right(lst, n)
            if idx == len(lst):
                lst.append(n)
            else:
                lst[idx] = n
            answer.append(idx+1)
        return answer