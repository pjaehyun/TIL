# 다른 풀이 참고해서 문제 해결
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @lru_cache(maxsize=None)
        def dfs(idx=0, prev=-inf):
            if idx == len(arr1):
                return 0
            res = inf
            if arr1[idx] > prev:
                res = dfs(idx+1, arr1[idx])
            
            new_idx = bisect_right(arr2, prev)
            if new_idx < len(arr2):
                res = min(res, 1 + dfs(idx+1, arr2[new_idx]))
            return res
        answer = dfs()
        return answer if answer != inf else -1