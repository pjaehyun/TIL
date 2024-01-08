import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    answer = 0
    planets = [list(map(int, input().split())) for _ in range(n)]

    for planet in planets:
        a, b, r = planet

        c1 = (x1-a)**2 + (y1-b)**2
        c2 = (x2-a)**2 + (y2-b)**2

        if c1 < r**2 and c2 > r**2:
            answer += 1
        
        if c1 > r**2 and c2 < r**2:
            answer += 1
    print(answer)