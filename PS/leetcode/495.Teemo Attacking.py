class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0

        start, end = timeSeries[0], timeSeries[0] + duration - 1

        for time in timeSeries[1:]:
            if start <= time <= end:
                end = time + duration - 1
            else:
                answer += (end - start + 1)
                start, end = time, time + duration - 1
                start, end
        answer += (end - start + 1)
        return answer