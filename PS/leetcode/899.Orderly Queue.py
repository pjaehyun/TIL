class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # k가 1보다 크다면 모든 문자열을 만들 수 있기 때문에 정렬된 문자열을 반환해주면 된다.
        if k > 1:
            return ''.join(sorted(s))
        
        result = s
        # k가 1일 때, 모든 문자를 한칸씩 뒤로 보내면서 가장 작은 문자열을 찾아서 반환한다.
        for _ in range(len(s)):
            s = s[1:] + s[0]
            result = min(result, s)
        return result
            