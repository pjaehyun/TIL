class Solution:
    def totalMoney(self, n: int) -> int:
        prefix = [x for x in range(1, 8)]
        answer = 0
        for i in range(1, 7):
            prefix[i] = prefix[i-1] + prefix[i]
        
        div = n // 7
        mod = n % 7
        for i in range(div):
            answer += prefix[-1] + (i * 7)
        if mod > 0:
            answer += (prefix[mod-1] + (mod * div))
        return answer