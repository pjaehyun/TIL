from collections import defaultdict

def solution(clothes):
    counter = defaultdict(int)
    result = 1
    for cloth, category in clothes:
        counter[category] += 1
    
    # (a + 1)(b + 1) = ab + a + b + 1
    # 여기서 구해야 하는 부분은 ab + a + b에 해당함
    # 모든 경우의 수를 구한 후 -1을 해줌
    for count in counter.values():
        result *= (1 + count)
    return result - 1