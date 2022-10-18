# Queue를 이용하여 풀었는데 코드 줄이고 시간복잡도 개선 필요
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(1, n):
            result = converter(result)
        return result
def converter(s):
    print(s)
    if len(s) == 1:
        return '1' + s
    new_string = []
    temp = []
    s = list(s)
    temp.append(s.pop(0))
    while s:
        t = s.pop(0)
        if temp[-1] == t:
            temp.append(t)
        else:
            new_string.append(str(len(temp)))
            new_string.append(str(temp[0]))

            temp.clear()
            temp.append(t)
    
    if len(temp) > 0:
        new_string.append(str(len(temp)))
        new_string.append(str(temp[0]))
    return ''.join(new_string)