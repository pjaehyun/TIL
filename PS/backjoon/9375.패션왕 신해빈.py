from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    answer = 1
    kinds = defaultdict(int)
    for _ in range(n):
        name, cate = map(str, input().split())
        kinds[cate] += 1
    
    for count in kinds.values():
        # +1 은 해당 부위를 아무것도 입지 않았을때
        answer *= (1 + count)
    # -1 은 모든 부위를 입지않은 경우는 제외해야됨
    print(answer - 1)