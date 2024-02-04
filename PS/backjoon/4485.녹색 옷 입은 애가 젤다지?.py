import sys
import heapq
input = sys.stdin.readline

def dijkstra(n):
    
    distances = [[float('inf')] * n for _ in range(n)]

    hq = []
    heapq.heappush(hq, (0, 0, graph[0][0]))

    while hq:
        x, y, d = heapq.heappop(hq)
        
        for xx, yy in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0 <= xx < n and 0 <= yy < n:
                if d + graph[xx][yy] < distances[xx][yy]:
                    distances[xx][yy] = d + graph[xx][yy]
                    heapq.heappush(hq, (xx, yy, d + graph[xx][yy]))
    return distances[n-1][n-1]

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]

    min_dist = dijkstra(n)
    
    print(f"Problem {t}: {min_dist}")

    t += 1