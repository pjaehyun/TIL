from collections import defaultdict, deque

def bfs(graph, start, visited):
    count = 1
    dq = deque()
    dq.append(start)
    visited.add(start)
    
    while dq:
        current = dq.popleft()
        
        for element in graph[current]:
            if element not in visited:
                visited.add(element)
                dq.append(element)
                count += 1
    return count
        

def solution(n, wires):
    answer = 1000
    for i in range(len(wires)):
        temp = wires[:]
        graph = defaultdict(list)
        visited = set()
        start = 0
        
        temp.pop(i)
        for x, y in temp:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(1, n+1):
            if graph[i]:
                start = i
                break
        count = bfs(graph, start, visited)
        answer = min(answer, abs((n - count) - count))
    return answer
        