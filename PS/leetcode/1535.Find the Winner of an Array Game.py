class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winners = defaultdict(int)
        winner = arr[0]
        
        for i in range(1, len(arr)):
            if winner > arr[i]:
                winners[winner] += 1
            else:
                winners[arr[i]] += 1
                winner = arr[i]
            if winners[winner] == k:
                break
        return winner