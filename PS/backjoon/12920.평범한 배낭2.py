# k의 갯수만큼 반복문을 돌면서 모든 경우를 넣도록 하였지만 중복으로 인한 오답
# 이를 해결하기 위해 2의 제곱수를 이용하여 문제를 해결함(2의 제곱수들의 합으로 모든 수를 만들 수 있다.)
N, M = map(int, input().split())

things = []

for i in range(N):
    v, c, k = map(int, input().split())
    
    # 2의 제곱수를 이용하여 물건들을 새로 세팅
    # Ex) k = 9일 떄, temp는 각 1, 2, 4, 2가 됨
    i = 1
    while k > 0:
        temp = min(i, k)
        things.append((v*temp, c*temp))
        i *= 2
        k -= temp

# kanpsack algorithm
dp = [[0] * (M+1) for _ in range(len(things) + 1)]

for i in range(1, len(things) + 1):
    for j in range(1, M+1):
        if things[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i-1][0]] + things[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])