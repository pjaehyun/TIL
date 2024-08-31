def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            now = array[i]
            result += 1
    return result


n = int(input())
array = [int(input()) for x in range(n)]

print(ascending(array))
array.reverse()
print(ascending(array))
