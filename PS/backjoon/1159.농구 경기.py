import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

count = [0] * 26

for _ in range(n):
    name = input().strip()
    count[ord(name[0]) - ord('a')] += 1

answer = ""

for i in range(26):
    if count[i] > 4:
        answer += chr(ord('a') + i)
print(answer) if answer != "" else print("PREDAJA")