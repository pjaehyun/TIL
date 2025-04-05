import sys
input = sys.stdin.readline

n = int(input())
bot=[]
cur=0
for i in range(n):
    a, b=map(int, input().split())
    bot.append([a, b])

cur += bot[0][1]

i=1

while i<n:
    cur+=1
    if cur%(bot[i][0]+bot[i][1])>=bot[i][1]:
        i+=1
    else:
        cur+=(bot[i][1]-cur%(bot[i][0]+bot[i][1])-1)
print(cur+1)