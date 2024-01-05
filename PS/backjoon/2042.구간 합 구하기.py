import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

tree = [0] * (n*4+1)

# build
def build(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2

    build(start, mid, node*2)
    build(mid+1, end, node*2+1)

    tree[node] = tree[node*2]+tree[node*2+1]

# update
def update(start, end, node, index, value):
    if index < start or index > end:
        return
    
    tree[node] += value
    if start == end:
        return
    
    mid = (start + end) // 2

    update(start, mid, node*2, index, value)
    update(mid+1, end, node*2+1, index, value)

    tree[node] = tree[node*2] + tree[node*2+1]
    return

def search(start, end, node, l, r):
    if l > end or r < start:
        return 0
    
    if l <= start and r >= end: return tree[node]

    mid = (start + end) // 2

    return search(start, mid, node*2, l, r) + search(mid+1, end, node*2+1, l, r)

build(0, n-1, 1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        temp = c - arr[b-1]
        arr[b-1] = c
        update(0, n-1, 1, b-1, temp)
    else:
        print(search(0, n-1, 1, b-1, c-1))