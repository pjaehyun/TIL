class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer = []
        
        def find(num, x, y):
            for i in range(len(matrix)):
                if num < matrix[i][y]:
                    return False
            
            for i in range(len(matrix[x])):
                if num > matrix[x][i]:
                    return False
            return True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if find(matrix[i][j], i, j):
                    answer.append(matrix[i][j])
        return answer