class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        colors = list(colors)
        move_count = defaultdict(int)
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                move_count[colors[i]] += 1
        if move_count['A'] > move_count['B']:
            return True
        else:
            return False