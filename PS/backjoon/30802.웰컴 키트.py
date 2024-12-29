import sys
input = sys.stdin.readline

n = int(input())
part = list(map(int,input().split()))
t,p = map(int,input().split())

ans = 0
for i in range(len(part)):
    if part[i]%t == 0:
        ans += int(part[i]/t)
    else:
        ans += (int(part[i]/t)+1)

print(ans)

ans2 = [int(sum(part)/p),sum(part)%p]
print(*ans2)