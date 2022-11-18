# 큐를 이용한 풀이
group = 0
for i in range(int(input())):
    s = list(input())
    temp = []
    temp.append(s.pop(0))
    check = True
    while s:
        char = s.pop(0)
        if temp[-1] != char and char in temp:
            check = False
            break
        if temp[-1] != char:
            temp.append(char)
    if check:
        group += 1
print(group)

# 인덱스를 이용한 풀이
N = int(input())
count = N

for _ in range(N):
    s = input()
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            continue
        elif s[i] in s[i+1:]:
            count -= 1
            break
print(count)