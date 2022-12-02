# Pypy3으로 제출
N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

start, end = 1, sum(trees)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for t in trees:
        if t > mid:
            cut += t - mid
    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
