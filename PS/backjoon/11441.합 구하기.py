import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, arr):
        self.tree = [0] * (n*4+1)
        self.arr = arr

    def build(self, s, e, node):
        
        if s == e:
            self.tree[node] = self.arr[s]
            return
        
        mid = (s + e) // 2

        self.build(s, mid, node*2)
        self.build(mid+1, e, node*2+1)

        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def search(self, s, e, i, j, node):
        if i > e or j < s:
            return 0
        
        if i <= s and j >= e:
            return self.tree[node]
        
        mid = (s + e) // 2

        return self.search(s, mid, i, j, node*2) + self.search(mid+1, e, i, j, node*2+1)

    
n = int(input())
arr = list(map(int, input().split()))

st = SegmentTree(n, arr)
st.build(0, n-1, 1)

m = int(input())

for _ in range(m):
    i, j = map(int, input().split())
    print(st.search(0, n-1, i-1, j-1, 1))