def solution(cacheSize, cities):
    arr = []
    answer = 0
    for c in cities:
        if c.lower() not in arr:
            answer += 5
            arr.append(c.lower())
            if len(arr) > cacheSize:
                arr.pop(0)
        else:
            answer += 1
            arr.pop(arr.index(c.lower()))
            arr.append(c.lower())
    return answer
            