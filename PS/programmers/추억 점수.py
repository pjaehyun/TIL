from collections import defaultdict
def solution(name, yearning, photo):
    dic = defaultdict(int)
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    answer = []
    for p in photo:
        temp = 0
        for e in p:
            temp += dic[e]
        answer.append(temp)
    return answer
