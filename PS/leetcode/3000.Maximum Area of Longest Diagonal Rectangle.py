class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        answer = 0 

        diag = 0

        for x, y in dimensions:
            t_diag, area = sqrt(x*x + y*y), x*y
            if t_diag > diag:
                answer = area
                diag = t_diag
            elif t_diag == diag and area > answer:
                answer = area
        return answer