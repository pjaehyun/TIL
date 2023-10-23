import sys
input = sys.stdin.readline

n, m = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

if m == 2:
    print(house[-1] - house[0])
else:
    l, r = 1, house[-1] - house[0]
    answer = 0
    while l < r:
        mid = (l + r) // 2
        
        curr = house[0]
        count = 1
        for i in range(1, n):
            if house[i] - curr >= mid:
                count += 1
                curr = house[i]
        if count >= m:
            answer = mid
            l = mid + 1
        elif count < m:
            r = mid
    print(answer)