class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(l, r, row, t):
            while l <= r:
                mid = (l + r) // 2
                if t < matrix[row][mid]:
                    r = mid - 1
                elif t > matrix[row][mid]:
                    l = mid + 1
                else:
                    return True
            return False
        
        row = 0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
        return bs(0, len(matrix[row]) - 1, row, target)
            