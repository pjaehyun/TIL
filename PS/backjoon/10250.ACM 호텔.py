for _ in range(int(input())):
    H, W, N = map(int, input().split())
    number = N // H + 1 if N % H != 0 else N // H
    floor = N % H * 100 if N % H != 0 else H * 100
    print(floor + number)