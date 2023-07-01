import heapq

def solution(people, limit):
    answer = 0
    
    people.sort()
    
    i, j = 0, len(people) - 1
    while i <= j:
        answer += 1
        if people[i] + people[j] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
    return answer