# 다른 풀이 참고
# Dp는 매번 틀리는듯 쉬운문제 더 많이 풀어봐야함
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        def bs_right(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                
                if target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        n = len(events)
        events.sort()
        starts = [x for x,y,z in events]
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            _next = bs_right(starts, events[i][1])
            for j in range(1, k+1):
                dp[i][j] = max(dp[i+1][j], events[i][2] + dp[_next][j-1])
        return dp[0][k]