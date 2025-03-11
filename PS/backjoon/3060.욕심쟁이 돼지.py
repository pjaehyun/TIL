import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    feed = int(input())
    pigs = list(map(int, input().split()))

    eat = sum(pigs)
    day = 1
    while eat <= feed:
        eat *= 4
        day += 1
    print(day)