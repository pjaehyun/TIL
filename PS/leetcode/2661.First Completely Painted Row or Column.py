class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        mat_idx = {}

        for i in range(m):
            for j in range(n):
                mat_idx[mat[i][j]] = (i, j)
        
        row = [0] * m
        col = [0] * n

        for i in range(len(arr)):
            row[mat_idx[arr[i]][0]] += 1
            col[mat_idx[arr[i]][1]] += 1
            if row[mat_idx[arr[i]][0]] == n or col[mat_idx[arr[i]][1]] == m:
                return i
        return -1
            