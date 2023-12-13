class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = defaultdict(int)
        col = defaultdict(int)
        
        special = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    special.append((i, j))
        answer = 0
        for x, y in special:
            if row[x] == 1 and col[y] == 1:
                answer += 1
        return answer