def solution(park, routes):
    coor = None
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                coor = [i, j]
                break
        if coor:
            break
    
    for command in routes:
        way, step = command.split()
        step = int(step)
        if way == 'E':
            # 오른쪽
            temp = coor[1]
            check = True
            for i in range(step):
                temp += 1
                if temp >= len(park[0]) or park[coor[0]][temp] == 'X':
                    check = False
                    break
            if check:
                coor[1] = temp
        elif way == 'W':
            # 왼쪽
            temp = coor[1]
            check = True
            for i in range(step):
                temp -= 1
                if temp < 0 or park[coor[0]][temp] == 'X':
                    check = False
                    break
            if check:
                coor[1] = temp
        elif way == 'N':
            # 위
            temp = coor[0]
            check = True
            for i in range(step):
                temp -= 1
                if temp < 0 or park[temp][coor[1]] == 'X':
                    check = False
                    break
            if check:
                coor[0] = temp
        else:
            # 아래
            temp = coor[0]
            check = True
            for i in range(step):
                temp += 1
                if temp >= len(park) or park[temp][coor[1]] == 'X':
                    check = False
                    break
            if check:
                coor[0] = temp
    return coor