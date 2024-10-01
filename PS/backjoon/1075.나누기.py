import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


for num in range(n - n % 100, n - n % 100 + 100):
    if num % m == 0:
        print(str(num)[-2:])
        break