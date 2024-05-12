class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        answer = [[0] * (m-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(m-2):
                max_value = 0
                for r in range(i, i+3):
                    for k in range(j, j+3):
                        max_value = max(max_value, grid[r][k])
                answer[i][j] = max_value
        return answer
            