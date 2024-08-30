X = input()
lst = []
result = []
num = ''
for x in X:
    if x == '-' or x == '+':
        lst.append(int(num))
        if x == '-' and x not in lst:
            lst.append(x)
        num = ''
        continue
    num += x
lst.append(int(num))

for i in range(len(lst)):
    if lst[i] == '-':
        for j in range(i+1, len(lst)):
            lst[j] -= (lst[j]*2)
    if lst[i] != '-':
        result.append(lst[i])
    
print(sum(result))