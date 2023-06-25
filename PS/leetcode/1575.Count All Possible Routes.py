# 첫번째 풀이(시간초과)
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        count = 0

        def back(start, fuel, finish):
            nonlocal count
            if fuel < 0:
                return

            if start == finish:
                count += 1
            
            for i in range(len(locations)):
                if i == start:
                    continue
                back(i, fuel - abs(locations[start] - locations[i]), finish)
        back(start, fuel, finish)
        return count


# 두번째 풀이(lru_cache를 사용하여 시간초과 해결)
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(start, fuel, finish):
            res = 0
            if fuel < 0:
                return 0

            if start == finish:
                res = 1
            
            for i in range(len(locations)):
                if i == start:
                    continue
                res += dfs(i, fuel - abs(locations[start] - locations[i]), finish)
            return res % (10**9+7)
        return dfs(start, fuel, finish)

            