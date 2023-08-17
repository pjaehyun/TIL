import sys
input = sys.stdin.readline

n = int(input())

i = 1
stack = []
answer = []
for _ in range(n):
    num = int(input())
    
    while not stack or stack and stack[-1] < num:
        stack.append(i)
        answer.append('+')
        i += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
if stack:
    print("NO")
else:
    for c in answer:
        print(c)