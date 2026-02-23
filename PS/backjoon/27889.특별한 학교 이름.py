import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

fullname = {
"NLCS": "North London Collegiate School",
"BHA": "Branksome Hall Asia",
"KIS": "Korea International School",
"SJA": "St. Johnsbury Academy"
}

n = input().strip()
print(fullname[n])