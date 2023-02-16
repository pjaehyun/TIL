# 총 소요시간 1시간
# 문제 이해하는 것에 시간을 상당히 소모함
def solution(queries):
    pea = [["Rr"], 
           ["RR", "Rr", "Rr", "rr"], 
           ["RR","RR","RR","RR","RR","Rr","Rr","rr","RR","Rr","Rr","rr","rr","rr","rr","rr"]]
    
    hybrid = ["RR", "Rr", "Rr", "rr"]
    
    def recursion(level, width):
        if level > 2:
            parent = recursion(level-1, width // 4)
            if parent == "Rr":
                return hybrid[width%4]
            else:
                return parent
        else:
            return pea[level][width]
        
    answer = []
    for query in queries:
        curr = recursion(query[0] - 1, query[1] - 1)
        answer.append(curr)
    return answer