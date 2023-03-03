def solution(elements):
    n = len(elements)
    prefixSum = [0] * n
    prefixSum[0] = elements[0]
    
    answer = set()
    
    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + elements[i]
    
    for i in range(n):
        answer.add(prefixSum[i])
        for j in range(i):
            answer.add(prefixSum[i] - prefixSum[j])
        
            if i == n-1:
                for k in range(j):
                    answer.add(prefixSum[i] - (prefixSum[j] - prefixSum[k]))
    return len(answer)