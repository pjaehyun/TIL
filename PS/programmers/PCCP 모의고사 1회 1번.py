# 총 소요시간 30분
from collections import Counter
def solution(input_string):
    if len(input_string) == 1:
        return "N"
    
    new_string = ""
    
    i, j = 0, 1
    while j < len(input_string):
        if input_string[i] == input_string[j]:
            j += 1
        else:
            new_string += input_string[i]
            i = j
            j += 1
    new_string += input_string[i]
    
    counter = Counter(new_string)
    
    answer = []
    for k, v in counter.items():
        if v > 1:
            answer.append(k)
    answer.sort()
    if not answer:
        return "N"
    return ''.join(answer)
