import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def minIndex(x, y):
    if x == -1: return y
    if y == -1: return x
    if arr[x] == arr[y]:
        return min(x, y)
    return x if arr[x] < arr[y] else y

def build(start, end, node):
    if start == end:
        tree[node] = start
        return

    mid = (start + end) // 2

    build(start, mid, node*2)
    build(mid+1, end, node*2+1)
    tree[node] = minIndex(tree[node*2], tree[node*2+1])
    return

def update(start, end, node, index):
    if index < start or index > end or start == end:
        return
    
    mid = (start + end) // 2

    update(start, mid, node*2, index)
    update(mid+1, end, node*2+1, index)

    tree[node] = minIndex(tree[node*2], tree[node*2+1])
    return


def search(start, end, node, l, r):
    if start > r or end < l: return -1
    
    if start >= l and end <= r: return tree[node]
    
    mid = (start + end) // 2

    return minIndex(search(start, mid, node*2, l, r), search(mid+1, end, node*2+1, l, r))

n = int(input())

arr = [0] + list(map(int, input().split()))

m = int(input())

tree = [0] * (4*n+1)

build(0, n, 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a == 1:
        arr[b] = c
        update(0, n, 1, b)
    else:
        print(search(0, n, 1, b, c))