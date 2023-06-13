class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, cols = defaultdict(int), defaultdict(int)

        for row in grid:
            rows[str(row)] += 1
        answer = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            answer += rows[str(col)]
        return answer