import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()

stack = []

for i in range(len(s)+1):
    if len(stack) >= len(bomb):
        if ''.join(stack[len(stack) - len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
    if i >= len(s):
        continue
    stack.append(s[i])

if not stack:
    print("FRULA")
else:
    print(''.join(stack))