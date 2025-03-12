import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
x = int(input())

store = []
seq = 1
loud = 0
bundegi = [0, 0]


while len(store) < 10001:
    
    for i in range(4):
        store.append(loud)
        loud ^= 1

    for i in range(seq+1):
        store.append(0)

    for i in range(seq+1):
        store.append(1)
    
    seq += 1

for i in range(10001):
    bundegi[store[i]] += 1
    if bundegi[x] == t:
        print(i % a)
        break