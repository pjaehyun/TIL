class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = defaultdict(int)
        onesCol = defaultdict(int)
        zerosRow = defaultdict(int)
        zerosCol = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
                else:
                    onesRow[i] += 1
                    onesCol[j] += 1
        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                answer[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return answer