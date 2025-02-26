import sys
input = sys.stdin.readline

cash = int(input())
md = list(map(int, input().split()))

jh = [cash, 0]
sm = [cash, 0]

gr = "i"
chart = []

for i in range(len(md)):
    jh_trade = jh[0] // md[i]
    jh[1] += jh_trade
    jh[0] -= (jh_trade * md[i])

for i in range(3, len(md)):
    if md[i-3] > md[i-2] > md[i-1] > md[i]:
        sm[1] += sm[0] // md[i]
        sm[0] = sm[0] % md[i]
    
    elif md[i-3] < md[i-2] < md[i-1] < md[i]:
        sm[0] += sm[1] * md[i]
        sm[1] = 0
j,s = jh[0] + jh[1] * md[-1], sm[0] + sm[1] * md[-1]

if j > s: print("BNP")
elif s > j: print("TIMING")
else: print("SAMESAME")