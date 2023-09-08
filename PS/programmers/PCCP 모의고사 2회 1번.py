# 제출 코드
def solution(command):
    x, y = 0, 0
    status = ["U", "R", "D", "L"]
    i = 0
    for c in command:
        if c == "G":
            if status[i] == "U":
                y += 1
            elif status[i] == "D":
                y -= 1
            elif status[i] == "R":
                x += 1
            else:
                x -= 1
        elif c == "B":
            if status[i] == "U":
                y -= 1
            elif status[i] == "D":
                y += 1
            elif status[i] == "R":
                x -= 1
            else:
                x += 1
        elif c == "R":
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
    return [x, y]

# 종료 후 리팩토링
def solution(command):
    x, y = 0, 0
    status = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = 0
    for c in command:
        if c == "G":
            x, y = x + status[i][0], y + status[i][1]
        elif c == "B":
            x, y = x - status[i][0], y - status[i][1]
        elif c == "R":
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
    return [x, y]