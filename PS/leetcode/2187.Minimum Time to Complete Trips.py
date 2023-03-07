class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        left, right = 1, min(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            temp = 0
            for i in range(len(time)):
                temp += (mid // time[i])
            if temp >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left