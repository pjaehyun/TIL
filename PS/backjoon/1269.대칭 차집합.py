import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

A, B = {x for x in list(map(int, input().split()))}, {x for x in list(map(int, input().split()))}

print(len((A | B) - (A & B)))