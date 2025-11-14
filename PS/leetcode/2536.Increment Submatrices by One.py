class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        diff = [[0] * n for _ in range(n)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if r2 + 1 < n: diff[r2 + 1][c1] -= 1
            if c2 + 1 < n: diff[r1][c2 + 1] -= 1
            if r2 + 1 < n and c2 + 1 < n: diff[r2 + 1][c2 + 1] += 1
        
        for i in range(n):
            for j in range(n):
                above = diff[i - 1][j] if i > 0 else 0
                left = diff[i][j - 1] if j > 0 else 0
                diag = diff[i - 1][j - 1] if i > 0 and j > 0 else 0
                diff[i][j] += above + left - diag
                
        return diff
