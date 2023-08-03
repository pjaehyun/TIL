class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letter = {
            '2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],'5': ['j','k','l'],
            '6': ['m','n','o'],'7': ['p','q','r','s'],'8': ['t','u','v'],'9': ['w','x','y','z']
        }
        answer = []
        def bt(comb, next):
            if len(next) == 0:
                answer.append(comb)
                return
            for neib in letter[next[0]]:
                bt(comb + neib, next[1:])
        bt("", digits)
        return answer