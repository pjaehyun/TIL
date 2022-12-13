import sys, heapq

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    min_q, max_q = [], []
    visited = [False] * k
    for i in range(k):
        temp = input().strip().split()
        command, n = temp[0], int(temp[1])
        
        if command == 'I':
            heapq.heappush(max_q, (-n, i))
            heapq.heappush(min_q, (n, i))
            visited[i] = True
        elif n == -1:
            # 최소힙의 가장 작은 값이 이미 삭제된 값일 때 제거
            while min_q and not visited[min_q[0][1]]:
                heapq.heappop(min_q)
            if min_q:
                visited[min_q[0][1]] = False
                heapq.heappop(min_q)
        else:
            # 최대힙의 가장 큰 값이 이미 삭제된 값일 때 제거
            while max_q and not visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                visited[max_q[0][1]] = False
                heapq.heappop(max_q)
              
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)

    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if not max_q and not min_q:
        print("EMPTY")
    else:
        max_value, min_value = heapq.heappop(max_q), heapq.heappop(min_q)
        print(-max_value[0], min_value[0])