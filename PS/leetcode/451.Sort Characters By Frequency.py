# 첫번째 풀이
class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted([(k, v) for k, v in Counter(s).items()], key=lambda x:x[1], reverse=True)
        answer = ""
        for k, v in s:
            answer += (k * v)
        return answer

# 두번째 풀이(한줄 코딩)
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(sorted([k * v for k, v in Counter(s).items()], key=lambda x:len(x), reverse=True))