import sys
input = sys.stdin.readline

n = int(input())
def fib(n):
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b

    return b

def fibonacci(n):
    return n-2

print(fib(n), fibonacci(n))