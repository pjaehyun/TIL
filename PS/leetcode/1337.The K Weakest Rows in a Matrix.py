# 첫번째 풀이
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        weakest = []
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            weakest.append((count, i))
        weakest.sort()
        
        answer = []

        for i in range(k):
            answer.append(weakest[i][1])
        return answer
    
# 코드 개선 및 시간복잡도 개선
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = sorted((sum(row), i) for i, row in enumerate(mat))
        answer = [weakest[i][1] for i in range(k)]
        return answer