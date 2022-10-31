class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            if (i+1) >= len(matrix):
                return True
            if matrix[i][0:len(matrix[i])-1] != matrix[i+1][1:len(matrix[i])]:
                return False
        