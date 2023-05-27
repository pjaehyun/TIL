# 다른 풀이 참고하여 풀이함
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3

        for i in range(n-1, -1, -1):
            one = stoneValue[i] - dp[(i+1) % 3]

            two = -float('inf')
            if i + 1 < n:
                two = stoneValue[i] + stoneValue[i+1] - dp[(i+2)%3]
            
            three = -float('inf')
            if i+2 < n:
                three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[(i+3)%3]
            
            dp[i%3] = max(one, two, three)
        
        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
