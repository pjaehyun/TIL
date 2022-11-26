class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, n = sorted(zip(startTime, endTime, profit)), len(startTime)
        dp = [0] * (n+1)

        for i in reversed(range(n)):            
            k = bs(jobs, jobs[i][1])
            dp[i] = max(jobs[i][2] + dp[k], dp[i+1])
        return dp[0]

# 이진 탐색
def bs(arr, n):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid][0] < n: low = mid + 1
        else: high = mid
    return low