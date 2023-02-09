import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

def count(n):
    if n == 1:
        return 1
    
    return 1+2*count(n-1)

def route(n,start,sub,end):
    if n == 1:
        print(start, end)
        return
    else:
        route(n-1, start, end, sub)
        print(start, end)
        route(n-1, sub, start, end)

print(count(N))
route(N,"1", "2", "3")