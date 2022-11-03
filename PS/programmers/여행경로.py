from collections import defaultdict

def solution(tickets):
    tickets_dict = defaultdict(list)
    result = []
    
    for start, end in tickets:
        tickets_dict[start].append(end)
    
    for key in tickets_dict.keys():
        tickets_dict[key].sort()
        
    def dfs(start):
        while tickets_dict[start]:
            end = tickets_dict[start].pop(0)
            dfs(end)
        
        if not tickets_dict[start]:
            result.append(start)
    
    # 출발지는 무조건 인천에서 출발
    dfs("ICN")
    return result[::-1]
    