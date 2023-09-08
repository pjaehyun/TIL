# 제출 코드
# 첫번째 풀이할 때 큐 문제인건 알았으나 큐로 해결하다가 완전탐색으로 변경(로직을 이상하게 짜서 변경함)
def solution(menu, order, k):
    n = len(order)
    arr = []
    answer = 0
    time = 0
    
    for i in range(n):
        if k * i > time:
            time = k * i + menu[order[i]]
        else:
            time += menu[order[i]]
        arr.append((i*k, time))
    
    for i in range(n):
        count = 0
        for j in range(i, n):
            if arr[i][1] <= arr[j][0]:
                break
            count += 1
        answer = max(answer, count)
    return answer

# 두번째 풀이(큐를 이용한 풀이)
from collections import deque
def solution(menu, order, k):
    n = len(order)
    dq = deque()
    answer = 0
    time = 0
    idx = 0

    while idx < n:
        if not dq:
            if (idx * k) > time:
                time = idx * k + menu[order[idx]]
            else: time += menu[order[idx]]
            idx += 1
        else:
            time += menu[dq.popleft()]
        while idx < n and time > (idx*k):
            dq.append(order[idx])
            idx += 1
        answer = max(answer, len(dq))
    return answer + 1