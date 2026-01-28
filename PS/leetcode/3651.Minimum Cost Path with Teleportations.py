from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        
        x_pos = defaultdict(list)
        max_val = 0
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                x_pos[val].append(i * n + j)
                max_val = max(max_val, val)
        
        dp = [[INF] * (m * n) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                if i > 0:
                    dp[0][pos] = min(dp[0][pos], dp[0][(i-1)*n+j] + grid[i][j])
                if j > 0:
                    dp[0][pos] = min(dp[0][pos], dp[0][i*n+j-1] + grid[i][j])
        
        for t in range(1, k + 1):
            suffix_min = [INF] * (max_val + 1)
            curr_min = INF
            for x in range(max_val, -1, -1):
                for idx in x_pos[x]:
                    curr_min = min(curr_min, dp[t-1][idx])
                suffix_min[x] = curr_min
            
            for i in range(m):
                for j in range(n):
                    pos = i * n + j
                    val = grid[i][j]
                    
                    dp[t][pos] = min(dp[t-1][pos], suffix_min[val])
                    
                    if i > 0:
                        dp[t][pos] = min(dp[t][pos], dp[t][(i-1)*n+j] + val)
                    if j > 0:
                        dp[t][pos] = min(dp[t][pos], dp[t][i*n+j-1] + val)
        
        return dp[k][m * n - 1]