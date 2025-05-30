import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def get_strahler(arr):

    count = {}
    max_value = max(arr)
    for e in arr:
        if e in count: count[e] += 1
        else: count[e] = 1

    if count[max_value] >= 2: return max_value + 1
    return max_value

t = int(input())

for _ in range(t):
    k, m, p = map(int, input().split())

    graph = defaultdict(list)
    in_degree = [0] * (m+1)
    strahlers = [[] for _ in range(m+1)]

    for _ in range(p):
        a, b = map(int, input().split())

        graph[a].append(b)
        in_degree[b] += 1
    
    dq = deque()

    for i in range(1, m+1):
        if in_degree[i] == 0:
            dq.append((i))
            strahlers[i].append(1)
    
    answer = 0

    while dq:
        
        for _ in range(len(dq)):
            curr = dq.popleft()
            
            strahler = get_strahler(strahlers[curr])
            answer = max(answer, strahler)
            for neib in graph[curr]:
                in_degree[neib] -= 1
                strahlers[neib].append(strahler)
                if in_degree[neib] == 0:
                    dq.append((neib))
    print(k, answer)
