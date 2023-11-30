import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

nums = []

for _ in range(n):
    nums.append(int(input()))

def build(start, end, node):
    if start == end:
        min_tree[node] = nums[start]
        max_tree[node] = nums[start]
        return
    
    mid = (start + end) // 2

    build(start, mid, node*2)
    build(mid+1, end, node*2+1)

    min_tree[node] = min(min_tree[node*2], min_tree[node*2+1])
    max_tree[node] = max(max_tree[node*2], max_tree[node*2+1])
    

def min_search(start, end, node, l, r):
    if start > r or end < l:
        return float('inf')
    
    if start >= l and end <= r:
        return min_tree[node]
    
    mid = (start + end) // 2

    return min(min_search(start, mid, node*2, l, r), min_search(mid+1, end, node*2+1, l, r))

def max_search(start, end, node, l, r):
    if start > r or end < l:
        return -1
    
    if start >= l and end <= r:
        return max_tree[node]
    
    mid = (start + end) // 2

    return max(max_search(start, mid, node*2, l, r), max_search(mid+1, end, node*2+1, l, r))

    

min_tree = [0] * (4*n+1)
max_tree = [0] * (4*n+1)

build(0, n-1, 1)
for _ in range(m):
    l, r = map(int, input().split())
    print(min_search(0, n-1, 1, l-1, r-1), max_search(0, n-1, 1, l-1, r-1))
