import sys
input = sys.stdin.readline

n = int(input())
mem = set()

for i in range(n):
    name, ent = map(str, input().split())

    if ent == "enter":
        mem.add(name)
    else:
        mem.remove(name)
mem = sorted(mem, reverse=True)
for m in mem:
    print(m)