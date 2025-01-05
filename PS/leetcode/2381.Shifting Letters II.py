class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        A = [0] * n
        
        for l, r, t in shifts:
            if t == 1:
                A[l] += 1
                if r + 1 < n:
                    A[r + 1] -= 1
            else:
                A[l] -= 1
                if r + 1 < n:
                    A[r + 1] += 1
        
        for i in range(1, n):
            A[i] += A[i - 1]
        
        result = []
        for i in range(n):
            shift = (A[i] % 26 + 26) % 26 
            ch = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(ord('a') + ch))
        
        return ''.join(result)