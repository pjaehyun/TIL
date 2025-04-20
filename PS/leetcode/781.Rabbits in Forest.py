class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)

        for a in answers:
            count[a+1] += 1
        
        answer = 0
        for k, v in count.items():
            answer += (k * int(math.ceil(v/k)))
        return answer