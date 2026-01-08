import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

def draw(x, y, line):
    if graph[x][y] == ".":
        graph[x][y] = line
    elif graph[x][y] != line:
        graph[x][y] = "+"

n = int(input())

footprint = input().strip()

graph = [["."] * n for _ in range(n)]

x, y = 0, 0
for i in range(len(footprint)):
    m = footprint[i]
    
    if m == "D":
        if x + 1 >= n:
            continue
        draw(x, y, "|")
        x = x+1
        draw(x, y, "|")
    elif m == "U":
        if x - 1 < 0:
            continue
        draw(x, y, "|")
        x = x-1
        draw(x, y, "|")
    elif m == "R":
        if y + 1 >= n:
            continue
        draw(x, y, "-")
        y = y+1
        draw(x, y, "-")
    else:
        if y - 1 < 0:
            continue
        draw(x, y, "-")
        y = y-1
        draw(x, y, "-")
for g in graph:
    print(''.join(g))