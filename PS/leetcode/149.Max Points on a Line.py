# 첫번째 풀이
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 1

        for x1, y1 in points:
            slope = defaultdict(int)
            # x2 - x1이 0일 떄 구분
            horizontal = 1
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x2 - x1 == 0:
                    horizontal += 1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    slope[m] += 1
            if slope:
                answer = max(answer, horizontal, max(slope.values()) + 1)
            else:
                answer = max(answer, horizontal)
        return answer

# 두번째 풀이(코드 줄이기)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for x1, y1 in points:
            slope = defaultdict(int)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x2 - x1 == 0:
                    slope[(x1)] += 1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    # 직선이 지나는 y절편을 이용하여 같은 기울기를 구분짓는다
                    slope[(m, y1 - m*x1)] += 1
            if slope:
                answer = max(answer, max(slope.values()))
        return answer + 1