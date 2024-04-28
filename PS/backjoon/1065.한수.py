N = int(input())

def arithmetic_sequence(n):
    temp = []
    while n != 0:
        temp.append(n % 10)
        n = n // 10
    temp.reverse()
    if len(temp) <= 2:
        return True
    temp[0] = temp[0] - temp[1]
    for i in range(2, len(temp)):
        if temp[i-1] - temp[i] == temp[0]:
            return True
        return False

result = 0
for i in range(1, N + 1):
    if arithmetic_sequence(i):
        result += 1
print(result)