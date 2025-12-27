import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    robots = [(input().strip(), i) for i in range(n)]
    
    k = len(robots[0][0])

    idx = 0
    
    winners = robots[:]
    while idx < k:
        temp = []

        rsp = {'R': [], 'S': [], 'P': []}

        for r, i in winners:
            rsp[r[idx]].append(i)
        if (rsp['R'] and rsp['S']) and not rsp['P']:
            for wi in rsp['R']:
                temp.append(robots[wi])
            winners = temp
        elif (rsp['S'] and rsp['P']) and not rsp['R']:
            for wi in rsp['S']:
                temp.append(robots[wi])
            winners = temp
        elif (rsp['P'] and rsp['R']) and not rsp['S']:
            for wi in rsp['P']:
                temp.append(robots[wi])
            winners = temp
        
        idx += 1
    if len(winners) > 1:
        print(0)
    else:
        print(winners[0][1] + 1)