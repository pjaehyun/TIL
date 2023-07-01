class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        _min = float('inf')
        dist = [0] * k

        def backtracking(x):
            nonlocal _min, dist
            if x == len(cookies):
                _min = min(max(dist), _min)
                return
            
            if _min <= max(dist):
                return

            for i in range(len(dist)):
                dist[i] += cookies[x]
                backtracking(x+1)
                dist[i] -= cookies[x]

        backtracking(0)
        return _min