N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
result = 0

for i in range(1, N-1):
    if costs[i-1] < costs[i]:
        costs[i] = costs[i-1]

for i in range(len(distances)):
    result += (costs[i] * distances[i])
print(result)