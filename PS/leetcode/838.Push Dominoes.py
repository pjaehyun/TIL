class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        right = -99
        i = 0
        
        while i < len(dominoes):
            if dominoes[i] == '.':
                i+=1
                continue
            elif dominoes[i] == 'L':
                if right < 0:
                    for j in range(i-1, -1, -1):
                        if dominoes[j] != '.':
                            break
                        else:
                            dominoes[j] = 'L'
                elif right >= 0 and right + 1 != i - 1 and right + 1 != i:
                    mid = ((i - right) // 2) + right
                    for j in range(right+1, mid+1 if (i-right) % 2 > 0 else mid):
                        dominoes[j] = 'R'
                    for j in range(mid+1, i):
                        dominoes[j] = 'L'
                right = -99
                i += 1
            elif dominoes[i] == 'R':
                if right >= 0:
                    for j in range(right+1, i+1):
                        dominoes[j] = 'R'
                right = i
                i+=1
        if right >= 0:
            for j in range(right+1, i):
                dominoes[j] = 'R'
                
        return ''.join(dominoes)
                