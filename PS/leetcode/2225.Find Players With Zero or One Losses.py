# 첫번째 코드
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        loser = defaultdict(int)
        answer = [[], []]

        for match in matches:
            winner.add(match[0])
            loser[match[1]] += 1
        
        for k, v in loser.items():
            winner.discard(k)
            if v == 1:
                answer[1].append(k)
        
        for w in sorted(winner):
            answer[0].append(w)
        answer[1].sort()

        return answer

# 두번째 코드(코드 라인 줄이기)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        winner, loser = [match[0] for match in matches], [match[1] for match in matches]
        set_winner, set_loser = set(winner), set(loser)
        
        answer.append(sorted(set_winner - set_loser))

        answer.append(sorted(k for k, v in Counter(loser).items() if v == 1))
        return answer
        