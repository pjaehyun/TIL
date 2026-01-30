class TrieNode(dict):
    __slots__ = ("sid",)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sid = -1


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)

        index = dict()
        for s in original + changed:
            if s not in index:
                index[s] = len(index)
        K = len(index)

        dist = [[math.inf] * K for _ in range(K)]
        for i in range(K):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u, v = index[o], index[c]
            dist[u][v] = min(dist[u][v], w)

        for k in range(K):
            for u in range(K):
                if dist[u][k] != math.inf:
                    for v in range(K):
                        if dist[k][v] != math.inf and dist[u][k] + dist[k][v] < dist[u][v]:
                            dist[u][v] = dist[u][k] + dist[k][v]

        trie = TrieNode()
        maxlen = 0
        for s, sid in index.items():
            node = trie
            for char in s:
                if char not in node:
                    node[char] = TrieNode()
                node = node[char]
            node.sid = sid
            maxlen = max(maxlen, len(s))

        def starts_map(s: str):
            result = [dict() for _ in range(n)]
            for i in range(n):
                node = trie
                for j in range(i, min(n, i + maxlen)):
                    if s[j] not in node:
                        break
                    node = node[s[j]]
                    if node.sid != -1:
                        result[i][j - i + 1] = node.sid

            return result

        src_starts = starts_map(source)
        tgt_starts = starts_map(target)

        dp = [0] + [math.inf] * n
        for i in range(n):
            if dp[i] == math.inf:
                continue

            if source[i] == target[i] and dp[i] < dp[i + 1]:
                dp[i + 1] = dp[i]

            sm, tm = src_starts[i], tgt_starts[i]
            if len(sm) == 0 or len(tm) == 0:
                continue

            for l in sm:
                if l not in tm:
                    continue
                d = dist[sm[l]][tm[l]]
                if d != math.inf and dp[i] + d < dp[i + l]:
                    dp[i + l] = dp[i] + d
            
        return dp[n] if dp[n] != math.inf else -1