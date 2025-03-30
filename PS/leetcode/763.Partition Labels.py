class Solution(object):
    def partitionLabels(self, s):
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        result = []
        farthest = left = 0

        for i, ch in enumerate(s):
            farthest = max(farthest, last_occurrence[ch])
            if i == farthest:
                result.append(farthest - left + 1)
                left = i + 1
        
        return result