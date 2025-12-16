class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        def merge(a, b):
            c = [0] * (budget + 1)
            for i in range(budget + 1):
                best = 0
                for j in range(i + 1):
                    v = a[i - j] + b[j]
                    if v > best:
                        best = v
                c[i] = best
            return c

        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        def dfs(u):
            cost = present[u]
            dcost = cost // 2

            sub0 = [0] * (budget + 1)
            sub1 = [0] * (budget + 1)
            for v in g[u]:
                c0, c1 = dfs(v)
                sub0 = merge(sub0, c0)
                sub1 = merge(sub1, c1)

            dp0 = sub0[:]
            dp1 = sub0[:]
            gain = future[u]

            for i in range(budget + 1):
                if i >= dcost:
                    dp1[i] = max(dp1[i], sub1[i - dcost] + gain - dcost)
                if i >= cost:
                    dp0[i] = max(dp0[i], sub1[i - cost] + gain - cost)
            return dp0, dp1

        return dfs(0)[0][budget]