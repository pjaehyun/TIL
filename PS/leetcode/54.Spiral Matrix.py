# 첫번째 풀이
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        
        way = "right"
        answer = []
        i, j = 0, 0
        w1, w2, h1, h2 = 0, n-1, 0, m-1
        check = 0
        while check < (m*n):
            if way == "right":
                if j == w2:
                    way = "down"
                    h1 += 1
                else:
                    answer.append(matrix[i][j])
                    j += 1
                    check += 1
            elif way == "down":
                if i == h2:
                    way = "left"
                    w2 -= 1
                else:
                    answer.append(matrix[i][j])
                    i += 1
                    check += 1
            elif way == "left":
                if j == w1:
                    way = "up"
                    h2 -= 1
                else:
                    answer.append(matrix[i][j])
                    j -= 1
                    check += 1
            else:
                if i == h1:
                    way = "right"
                    w1 += 1
                else:
                    answer.append(matrix[i][j])
                    i -= 1
                    check += 1
        return answer

# 두번째 풀이(코드 개선)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        
        way = "right"
        answer = []
        w1, w2, h1, h2 = 0, n - 1, 0, m - 1
        while h1 <= h2 and w1 <= w2:
            if way == "right":
                for i in range(w1, w2+1):
                    answer.append(matrix[h1][i])
                way = "down"
                h1 += 1
            elif way == "down":
                for i in range(h1, h2+1):
                    answer.append(matrix[i][w2])
                way = "left"
                w2 -= 1
            elif way == "left":
                for i in range(w2, w1-1, -1):
                    answer.append(matrix[h2][i])
                way = "up"
                h2 -= 1
            else:
                for i in range(h2, h1-1, -1):
                    answer.append(matrix[i][w1])
                way = "right"
                w1 += 1
        return answer