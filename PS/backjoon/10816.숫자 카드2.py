import sys
from collections import defaultdict

input = sys.stdin.readline

N, N_list = int(input()), list(map(int, input().split()))

M, M_list = int(input()), list(map(int, input().split()))

card_count = defaultdict(int)

for num in N_list:
    card_count[num] += 1

for num in M_list:
    print(card_count[num], end=" ")