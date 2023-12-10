class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        answer = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                answer[j][i] = matrix[i][j]
        return answer