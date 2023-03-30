# 첫번째 풀이
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]
        i, j = 1, -1
        answer = []
        up = True
        while i < len(mat) and j < len(mat[0]):
            if i == len(mat) - 1 and j == len(mat[0]) -1:
                break
            if up:
                i -= 1
                j += 1
                
                if (i < 0 and j >= len(mat[0])) or (0 <= i < len(mat) and j >= len(mat[0])):
                    i += 2
                    j -= 1
                    up = False
                elif i < 0 and 0 <= j < len(mat[0]):
                    i += 1
                    up = False
                answer.append(mat[i][j])
            else:
                i += 1
                j -= 1

                if (j < 0 and i >= len(mat)) or (0 <= j < len(mat[0]) and i >= len(mat)):
                    i -= 1
                    j += 2
                    up = True
                elif j < 0 and 0 <= i < len(mat):
                    j += 1
                    up = True
                answer.append(mat[i][j])
                
        return answer

# 두번째 풀이(코드개선)        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        count = 0
        x, y = 0, 0
        answer = []
        up = True

        while count < m*n:
            if 0 <= x < m and 0 <= y < n:
                answer.append(mat[x][y])
                count += 1
            if up:
                if x - 1 >= 0 and y + 1 < n:
                    x -= 1
                    y += 1
                else:
                    up = False
                    y += 1
            else:
                if x + 1 < m and y - 1 >= 0:
                    x += 1
                    y -= 1
                else:
                    up = True
                    x += 1
        return answer