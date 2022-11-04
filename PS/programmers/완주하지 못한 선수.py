from collections import Counter

def solution(participant, completion):
    counter_completion = Counter(completion)
    for player in participant:
        if player in counter_completion:
            if counter_completion[player] == 0:
                return player
            counter_completion[player] -= 1
        else:
            return player
        