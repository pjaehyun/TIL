def solution(n, m, section):
    answer = 1
    first = section[0]
    for i in range(1, len(section)):
        if section[i] - first < m:
            continue
        else:
            first = section[i]
            answer += 1
    return answer