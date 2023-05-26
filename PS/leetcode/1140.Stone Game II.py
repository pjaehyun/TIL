class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf_sum = [0] * (n+1)
        suf_sum[n-1] = piles[n-1]
        for i in range(n-2, -1, -1):
            suf_sum[i] = suf_sum[i+1] + piles[i]
        
        dp = [[0] * (n+1) for _ in range(n)]

        for i in range(n-1, -1, -1):
            for m in range(1, n+1):
                if i+2*m >= n:
                    dp[i][m] = suf_sum[i]
                else:
                    for x in range(1, 2*m+1):
                        temp = dp[i+x][max(x,m)]
                        dp[i][m] = max(dp[i][m], suf_sum[i]-temp)
        return dp[0][1]