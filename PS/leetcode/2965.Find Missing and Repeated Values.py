class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        _dict = defaultdict(int)
        answer = [0, 0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                _dict[grid[i][j]] += 1
                if _dict[grid[i][j]] == 2:
                    answer[0] = grid[i][j]
        

        for i in range(1, 2501):
            if _dict[i] == 0:
                answer[1] = i
                break
        return answer