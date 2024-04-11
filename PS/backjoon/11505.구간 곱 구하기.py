import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

class SegmentTree:
    def __init__(self, n, arr):
        self.tree = [0] * (n * 4 + 1)
        self.arr = arr

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2

        self.build(start, mid, node*2)
        self.build(mid + 1, end, node*2+1)

        self.tree[node] = self.tree[node*2] * self.tree[node*2+1] % 1000000007

    def update(self, start, end, index, curr, node):
        if index < start or index > end:
            return
        
        if start == end:
            self.tree[node] = curr
            return
        
        mid = (start + end) // 2

        self.update(start, mid, index, curr, node*2)
        self.update(mid + 1, end, index, curr, node*2+1)

        self.tree[node] = self.tree[node*2] * self.tree[node*2+1] % 1000000007


    def search(self, start, end, left, right, node):
        if left > end or right < start:
            return 1
        
        if left <= start and right >= end:
            return self.tree[node]
        
        mid = (start + end) // 2

        return self.search(start, mid, left, right, node*2) * self.search(mid + 1, end, left, right, node*2+1) % 1000000007

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

st = SegmentTree(n, arr)
st.build(0, n-1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        st.update(0, n-1, b-1, c, 1)
    else:
        print(st.search(0, n-1, b-1, c-1, 1))