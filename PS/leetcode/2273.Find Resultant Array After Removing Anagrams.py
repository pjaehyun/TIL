class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        op = [words.pop(0)]
        prev = ''.join(sorted([k*v for k, v in Counter(op[-1]).items()]))
        while words:
            curr = words.pop(0)

            ana = ''.join(sorted([k*v for k, v in Counter(curr).items()]))
            
            if prev == ana: continue
            else:
                op.append(curr)
                prev = ana
        return op