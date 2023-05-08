class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l, r = 0, len(mat) - 1
        total = 0

        for i in range(len(mat)):
            if l != r:
                total += mat[i][l] + mat[i][r]
            else:
                total += mat[i][l]
            l += 1
            r -= 1
        return total