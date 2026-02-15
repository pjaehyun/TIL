import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

a, b = map(int, input().split())

while True:
    if a >= 5: 
      print("yj") 
      break
    
    b += a

    if b >= 5:
       print("yt")
       break
    
    a += b