import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []

for _ in range(p):
    level, _id = map(str, input().strip().split())
    level = int(level)

    is_none = True
    for i in range(len(rooms)):
        if len(rooms[i]) == m:
            continue
        if rooms[i][0][0] - 10 <= level <= rooms[i][0][0] + 10:
            is_none = False
            rooms[i].append((level, _id))
            break
    if is_none: rooms.append([(level, _id)])

for room in rooms:
    room.sort(key=lambda x:x[1])

    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for part in room:
        print(part[0], part[1])