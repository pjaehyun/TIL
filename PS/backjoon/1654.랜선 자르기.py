K, N = map(int, input().split())

cables = []
for _ in range(K):
    cables.append(int(input()))

cables.sort()

start, end = 1, cables[-1]

while start <= end:
    mid = (start + end) // 2
    count = 0
    for cable in cables:
        count += cable // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)