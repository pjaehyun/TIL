def solution(targets):
    targets.sort(key=lambda x:x[1])
    answer = [targets[0]]
    for target in targets[1:]:
        if answer[-1][1] <= target[0]:
            answer.append(target)
    return len(answer)
            