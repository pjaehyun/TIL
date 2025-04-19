import sys
input = sys.stdin.readline

n, l, w, h = map(int, input().split())

s, e = 0, max(l, w, h)
answer = 0
for _ in range(10000):
    mid = (s + e) / 2
    count = (l//mid)*(w//mid)*(h//mid)
    
    if count >= n:
        answer = mid
        s = mid
    else:
        e = mid
print(answer)