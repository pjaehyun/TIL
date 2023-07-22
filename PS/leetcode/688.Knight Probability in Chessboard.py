class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1

        for step in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    for di, dj in [[i+1,j+2],[i+1,j-2],[i+2,j+1],[i+2,j-1],[i-1,j+2],[i-1,j-2],[i-2,j-1],[i-2,j+1]]:
                        if 0 <= di < n and 0 <= dj < n:
                            dp[step][i][j] += (dp[step-1][di][dj] / 8.0)
        answer = 0
        for i in range(n):
            for j in range(n):
                answer += dp[k][i][j]
        return answer