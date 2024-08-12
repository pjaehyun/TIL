from collections import deque
k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    cnt = 0
    lst = deque([(val, idx) for idx, val in enumerate(list(map(int, input().split())))])
    if len(lst) == 1:
        print(1)
        continue
    while lst:
        prt = lst.popleft()
        if lst and prt[0] <  max(lst)[0]:
            lst.append(prt)
        elif lst and prt[0] >= max(lst)[0] and prt[1] == m:
            cnt += 1
            break
        else:
            cnt += 1
    print(cnt)
