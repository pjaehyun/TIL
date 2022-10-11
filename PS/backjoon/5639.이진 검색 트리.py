import sys
sys.setrecursionlimit(1000000)

lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

def postorder(start,end):
    if start > end:
        return
    mid = end+1  
    for i in range(start+1,end+1):
        if lst[start] < lst[i]:
            mid = i
            break
    
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(lst[start])

postorder(0,len(lst)-1)