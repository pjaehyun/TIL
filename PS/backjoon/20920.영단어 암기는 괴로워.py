from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = defaultdict(int)

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words[word] += 1

answer = sorted([(k, v) for k, v in words.items()], key=lambda x:(-x[1], -len(x[0]), x[0]))

for a in answer:
    print(a[0])