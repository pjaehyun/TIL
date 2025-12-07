import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

l_key = {
    'q': (0, 0),
    'w': (0, 1),
    'e': (0, 2),
    'r': (0, 3),
    't': (0, 4),
    'a': (1, 0),
    's': (1, 1),
    'd': (1, 2),
    'f': (1, 3),
    'g': (1, 4),
    'z': (2, 0),
    'x': (2, 1),
    'c': (2, 2),
    'v': (2, 3)
    }
r_key = {
    'y': (0, 0),
    'u': (0, 1),
    'i': (0, 2),
    'o': (0, 3),
    'p': (0, 4),
    'h': (1, 0),
    'j': (1, 1),
    'k': (1, 2),
    'l': (1, 3),
    'b': (2, -1),
    'n': (2, 0),
    'm': (2, 1)
    }

sl, sr = map(str, input().split())

s = input().strip()

prev_l, prev_r = l_key[sl], r_key[sr]

total = 0
for i in range(len(s)):
    if s[i] in l_key:
        x1, y1 = prev_l
        x2, y2 = l_key[s[i]]
        distance = abs(x1-x2) + abs(y1-y2)
        total += (distance + 1)
        prev_l = [x2, y2]
    else:
        x1, y1 = prev_r
        x2, y2 = r_key[s[i]]
        distance = abs(x1-x2) + abs(y1-y2)
        total += (distance + 1)
        prev_r = x2, y2
print(total)