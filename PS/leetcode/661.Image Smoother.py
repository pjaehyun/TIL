class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                _sum = 0
                for x, y in [(i, j),(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]:
                    if 0 <= x < m and 0 <= y < n:
                        count += 1
                        _sum += img[x][y]
                avg = _sum // count
                answer[i][j] = avg
        return answer