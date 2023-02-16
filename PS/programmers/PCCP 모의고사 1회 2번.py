# 총 소요시간 30분
def solution(ability):
    sports = [[ability[z][x] for z in range(len(ability))] for x in range(len(ability[0]))]
    
    visited = set()
    answer = 0
    
    def backtracking(idx, value, n):
        nonlocal answer
        if idx == n - 1:
            answer = max(answer, value)  
        else:    
            for j in range(len(sports[0])):
                if j not in visited:
                    visited.add(j)
                    backtracking(idx+1, value + sports[idx+1][j], n)
                    visited.remove(j)
    
    for i in range(len(sports[0])):
        if i not in visited:
            visited.add(i)
            backtracking(0, sports[0][i], len(sports))
            visited.remove(i)
    return answer
    
    