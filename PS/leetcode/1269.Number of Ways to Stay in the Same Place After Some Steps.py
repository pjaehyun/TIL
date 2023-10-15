class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        m = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(pos, steps):
            if pos < 0 or pos > steps or pos > arrLen - 1: return 0

            if steps == 0: return pos == 0

            return (
                dfs(pos -1, steps - 1) + 
                dfs(pos, steps - 1) + 
                dfs(pos +1, steps - 1)
            ) % m
        return dfs(0, steps)