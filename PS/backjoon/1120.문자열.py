import sys
input = sys.stdin.readline

a,b=input().split()

result=[]
for i in range(len(b)-len(a)+1):
    cnt=0
    for j in range(len(a)):
        if a[j]!=b[j+i]:
            cnt+=1
    result.append(cnt)
print(min(result))