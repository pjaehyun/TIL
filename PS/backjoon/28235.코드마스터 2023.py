import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

cheering = {
"SONGDO": "HIGHSCHOOL",
"CODE":"MASTER",
"2023":"0611",
"ALGORITHM":"CONTEST"
}

n = input().strip()
print(cheering[n])