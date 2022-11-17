def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    a_devisor_list = get_all_devisor(arrayA[0])
    b_devisor_list = get_all_devisor(arrayB[0])
    
    a = get_max_integer(arrayA, arrayB, a_devisor_list)
    b = get_max_integer(arrayB, arrayA, b_devisor_list)
    
    answer = max(a, b)
    
    return answer

def get_max_integer(array1, array2, devisors):
    for devisor in devisors:
        if devisor == 1:
            continue
        check = True
        for i in range(len(array1)):
            if array1[i] % devisor != 0 or array2[i] % devisor == 0:
                check = False
                break
        if check:
            return devisor
    return 0

def get_all_devisor(num):
    result = []
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            result.append(i)
            if i ** 2 != num:
                result.append(num // i)
    return sorted(result, reverse=True)
    