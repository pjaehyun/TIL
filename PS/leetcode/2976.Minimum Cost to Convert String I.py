class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0
        
        for o, c, co in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], co)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        answer = 0
        for i in range(len(source)):
            answer += dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return answer if answer != float('inf') else -1
