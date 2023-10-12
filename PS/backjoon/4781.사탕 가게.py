import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == 0 and m == 0:
        break
    candies = []
    n, m = int(n), int(m * 100)
    for _ in range(int(n)):
        c, p = map(float, input().split())
        candies.append((int(c), int(p*100 + 0.5)))
    
    dp = [0] * (m+1)
    for i in range(1, m+1):
        for j in range(n):
            if i - candies[j][1] >= 0:
                dp[i] = max(dp[i], dp[i - candies[j][1]] + candies[j][0])
    print(dp[m])