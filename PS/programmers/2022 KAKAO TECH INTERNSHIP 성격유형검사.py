def solution(survey, choices):
    indi = {'RT': {'R': 0, 'T': 0}, 'CF': {'C': 0, 'F': 0}, 'JM': {'J': 0, 'M': 0}, 'AN': {'A': 0, 'N': 0}}
    result = []
    for i in range(len(survey)):
        s = list(survey[i])
        score = choices[i] - 4
        if score > 0:
            indi[''.join(sorted(s))][s[1]] += score
        else:
            indi[''.join(sorted(s))][s[0]] += abs(score)
        
    for k1, v1 in indi.items():
        k1 = list(k1)
        if v1[k1[0]] >= v1[k1[1]]:
            result.append(k1[0])
        else:
            result.append(k1[1])
    return ''.join(result)