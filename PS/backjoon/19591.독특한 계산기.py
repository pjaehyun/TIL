import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

def calc(a, b, o):
    if o == "/":
        return math.trunc(a / b)
    
    if o == "*":
        return a * b
    
    if o == "+":
        return a + b
    
    if o == "-":
        return a - b


s = input().strip()

nums = deque()
ops = deque()

num = ""

for i in range(len(s)):
    if num == "" and not s[i].isdigit():
        num += s[i]
        continue

    if s[i].isdigit():
        num += s[i]
    else:
        nums.append(int(num))
        ops.append(s[i])
        num = ""
nums.append(int(num))

f = {"*", "/"}
x = {"+", "-"}

while len(ops) > 1:
    a, b = nums[0], nums[1]
    c, d = nums[-2], nums[-1]

    op1, op2 = ops[0], ops[-1]

    if (op1 in f and op2 in f) or (op1 in x and op2 in x):
        c1 = calc(a, b, op1)
        c2 = calc(c, d, op2)
        if c1 >= c2:
            nums.popleft()
            nums.popleft()
            ops.popleft()
            nums.appendleft(c1)
        else:
            nums.pop()
            nums.pop()
            ops.pop()
            nums.append(c2)
    elif op1 in f and op2 in x:
        c1 = calc(a, b, op1)
        nums.popleft()
        nums.popleft()
        ops.popleft()
        nums.appendleft(c1)
    elif op1 in x and op2 in f:
        c2 = calc(c, d, op2)
        nums.pop()
        nums.pop()
        ops.pop()
        nums.append(c2)

if len(nums) > 1:
    print(calc(nums[0], nums[1], ops[0]))
else:
    print(nums[0])