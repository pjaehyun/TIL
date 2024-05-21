import sys
input = sys.stdin.readline

n = input().strip()

if "0" not in n:
    print(-1)

else:
    num_sum = 0
    for i in range(len(n)):
        num_sum += int(n[i])

    if num_sum % 3 != 0:
        print(-1)
    
    else:
        sorted_num = sorted(n, reverse=True)
        answer = "".join(sorted_num)
        print(answer)