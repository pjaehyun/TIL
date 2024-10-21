class Solution(object):
    def maxUniqueSplit(self, s):
        def dfs(start, seen):
            if start == len(s):
                return 0

            max_splits = 0
            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]

                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, 1 + dfs(i, seen))
                    seen.remove(substring)

            return max_splits

        return dfs(0, set())