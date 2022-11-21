A, B = map(str, input().split())

if len(A) != len(B):
    if len(A) < len(B):
        A = ('0' * (len(B) - len(A))) + A
    else:
        B = ('0' * (len(A) - len(B))) + B

A, B = list(reversed(A)), list(reversed(B)) 

answer = []
carry = 0

for i in range(len(A)):
    num = int(A[i]) + int(B[i]) + carry
    answer.append(str(num % 10))
    carry = num // 10

if carry > 0:
    answer.append(str(carry))

answer.reverse()
print(''.join(answer))