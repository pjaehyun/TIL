import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n-1)]

s = int(input())

sums = sum(arr)
an = (sums - s) // (n-2)
for i in range(n-1):
    print(arr[i] - an)
print(an)