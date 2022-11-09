def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack or s[i] == '(':
            stack.append(s[i])
            continue
        if s[i] == ')' and stack[-1] == '(':
            stack.pop()
            continue
    if stack:
        return False
    return True
        