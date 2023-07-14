# 시간초과가 계속 발생하여 다른 풀이 참고
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        dp = defaultdict(int)
        answer = 0
        for i in range(n):
            num = arr[i] 
        
            if num - difference in dp:
                dp[num] = dp[num-difference] + 1
            else:
                dp[num] = 1
            
            answer = max(answer, dp[num])
        return answer