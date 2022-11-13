def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        h = i+1
        for j in range(len(citations)):
            if citations[j] >= h:
                if h <= len(citations[j:]):
                    answer = h
                    break
    return answer