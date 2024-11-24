class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_min = float('inf')
        cnt = 0
        abs_sum = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    cnt += 1
                
                abs_min = min(abs(matrix[i][j]), abs_min)
                abs_sum += abs(matrix[i][j])
            
        return abs_sum if cnt % 2 == 0 else abs_sum - abs_min * 2