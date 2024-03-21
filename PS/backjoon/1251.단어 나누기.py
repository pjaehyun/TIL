import sys
input = sys.stdin.readline

word = input().strip()
ans_list = []
for i in range(1,len(word)-1):
	ans = []
	for j in range(i+1,len(word)):
		ans = ((word[0:i:])[::-1])+((word[i:j:])[::-1])+((word[j::])[::-1])
		ans_list.append(ans)

ans_list.sort()
print(ans_list[0])