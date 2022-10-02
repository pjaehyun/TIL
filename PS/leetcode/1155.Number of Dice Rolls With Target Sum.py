# 생각하다가 풀이가 안되서 풀이과정 보면서 풀었음
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dynamic(n, k, t):
            if n == 0 and t == 0: return 1
            if n == 0: return 0

            answer = 0

            for i in range(1, k + 1):
                answer += dynamic(n - 1, k, t - i)
            return answer % (10**9 + 7)
        return dynamic(n, k, target)
