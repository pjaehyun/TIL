import sys
input = sys.stdin.readline

def fgcd(a,b):
    while b > 0:
        a,b = b,a % b
    return a

n = int(input())
cnt = 0

arr = sorted([int(sys.stdin.readline()) for _ in range(n)])

sub = []
for i in range(len(arr) -1):
    sub.append(arr[i+1] - arr[i])

gcd = sub[0]
for i in range(1, len(sub)):
    gcd = fgcd(gcd, sub[i])
    
    
for j in sub:
    cnt += j // gcd -1

print(cnt)