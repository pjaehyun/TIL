import sys
input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    command = input().rstrip()
    
    if len(command) > 2:
        stack.append(int(command[2:]))
    elif command == '2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(1 if len(stack)==0 else 0)
    elif command == '5':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])