def solution(array, commands):
    answer = []
    filtered = []
    for command in commands:
        filtered = array[command[0]-1:command[1]]        
        filtered.sort()
        answer.append(filtered[command[2] - 1])
    return answer