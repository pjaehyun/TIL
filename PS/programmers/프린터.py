def solution(priorities, location):
    priorities = [(p, idx) for idx, p in enumerate(priorities)]
    answer = 0
    while priorities:
        priority, index = priorities.pop(0)
        if check_max(priority, priorities):
            answer += 1
            if index == location:
                return answer
        else:
            priorities.append((priority, index))
        
    
def check_max(num, arr):
    for a in arr:
        if a[0] > num:
            return False
    return True
    
    