class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)

        tree = defaultdict(list)
        for end, start in enumerate(parent):
            tree[start].append(end)
        
        answer = 1
        def dfs(node):
            nonlocal answer
            res = 1
            for child in tree[node]:
                l = dfs(child)

                if s[node] != s[child]:
                    # 가장 긴 노드의 길이
                    answer = max(answer, res + l)
                    # 현재 연결된 노드의 길이
                    res = max(res, l+1)
            return res
        dfs(0)
        return answer