import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

p_maxH = []
p_minH = []

g_minH = defaultdict(list)
g_maxH = defaultdict(list)

l_minH = defaultdict(list)
l_maxH = defaultdict(list)

pdict = defaultdict(int)
gdict = defaultdict(int)

n = int(input())

for _ in range(n):
    p, l, g = map(int, input().split())
    
    heapq.heappush(p_maxH, (-l, -p, g))
    heapq.heappush(p_minH, (l, p, g))

    heapq.heappush(g_maxH[g], (-l, -p, g))
    heapq.heappush(g_minH[g], (l, p, g))

    heapq.heappush(l_maxH[l], (-l, -p, g))
    heapq.heappush(l_minH[l], (l, p, g))

    pdict[p] = l
    gdict[p] = g

m = int(input())
for _ in range(m):
    command = list(map(str, input().strip().split()))
    
    if command[0] == "add":
        p, l, g = int(command[1]), int(command[2]), int(command[3])
        heapq.heappush(p_maxH, (-l, -p, g))
        heapq.heappush(p_minH, (l, p, g))

        heapq.heappush(g_maxH[g], (-l, -p, g))
        heapq.heappush(g_minH[g], (l, p, g))

        heapq.heappush(l_maxH[l], (-l, -p, g))
        heapq.heappush(l_minH[l], (l, p, g))

        pdict[p] = l
        gdict[p] = g
    elif command[0] == "recommend":
        g = int(command[1])
        if command[2] == "1":
            while g_maxH[g] and (pdict[-g_maxH[g][0][1]] != - g_maxH[g][0][0] or gdict[-g_maxH[g][0][1]] != g_maxH[g][0][2]):
                heapq.heappop(g_maxH[g])
            print(-g_maxH[g][0][1])
        else:
            while g_minH and (pdict[g_minH[g][0][1]] != g_minH[g][0][0] or gdict[g_minH[g][0][1]] != g_minH[g][0][2]):
                heapq.heappop(g_minH[g])
            print(g_minH[g][0][1])
    elif command[0] == "recommend2":
        if command[1] == "1":
            while p_maxH and (pdict[-p_maxH[0][1]] != -p_maxH[0][0] or gdict[-p_maxH[0][1]] != p_maxH[0][2]):
                heapq.heappop(p_maxH)
            print(-p_maxH[0][1])
        else:
            while p_minH and (pdict[p_minH[0][1]] != p_minH[0][0] or gdict[p_minH[0][1]] != p_minH[0][2]):
                heapq.heappop(p_minH)
            print(p_minH[0][1])
    elif command[0] == "recommend3":
        l = int(command[2])
        flag = False
        if command[1] == "1":
            for i in range(l, 101):
                while l_minH[i] and (pdict[l_minH[i][0][1]] != l_minH[i][0][0] or gdict[l_minH[i][0][1]] != l_minH[i][0][2]):
                    heapq.heappop(l_minH[i])
                if l_minH[i]:
                    print(l_minH[i][0][1])
                    flag = True
                    break
        else:
            for i in range(l-1, 0, -1):
                while l_maxH[i] and (pdict[-l_maxH[i][0][1]] != -l_maxH[i][0][0] or gdict[-l_maxH[i][0][1]] != l_maxH[i][0][2]):
                    heapq.heappop(l_maxH[i])
                if l_maxH[i]:
                    print(-l_maxH[i][0][1])
                    flag = True
                    break
        if not flag:
            print(-1)
    else:
        p = int(command[1])
        pdict[p] = 0
        gdict[p] = 0