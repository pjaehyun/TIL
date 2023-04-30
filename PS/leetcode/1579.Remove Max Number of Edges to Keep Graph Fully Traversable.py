# 다른 풀이 참고하여 풀이
class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n+1)]
        self.rank = [0] * (n+1)

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
            return 1
        return 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key=lambda x:x[0], reverse=True)
        alice = UnionFind(n)
        bob = UnionFind(n)
        alice_edge, bob_edge = 0, 0
        removes = 0

        for type, x, y in edges:
            if type == 3:
                if alice.union(x, y) == 1:
                    bob.union(x, y)
                    alice_edge += 1
                    bob_edge += 1
                else:
                    removes += 1
            elif type == 2:
                if bob.union(x, y) == 1:
                    bob_edge += 1
                else:
                    removes += 1
            else:
                if alice.union(x, y) == 1:
                    alice_edge += 1
                else:
                    removes += 1
        return removes if bob_edge == alice_edge == n-1 else -1