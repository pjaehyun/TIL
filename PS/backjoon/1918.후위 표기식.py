import sys

from collections import deque

input = sys.stdin.readline

S = input().rstrip()

stack = []

answer = []
for c in S:
    if 65 <= ord(c) <= 90:
        answer.append(c)
    else:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                answer.append(temp)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.append(c)
        else:
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer.append(stack.pop())
            stack.append(c)
while stack:
    answer.append(stack.pop())
print(''.join(answer))
