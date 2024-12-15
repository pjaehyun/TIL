class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def pass_ratio_gain(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali
        
        heap = []
        for passi, totali in classes:
            gain = pass_ratio_gain(passi, totali)
            heappush(heap, (-gain, passi, totali))
        
        for _ in range(extraStudents):
            gain, passi, totali = heappop(heap)
            passi += 1
            totali += 1
            new_gain = pass_ratio_gain(passi, totali)
            heappush(heap, (-new_gain, passi, totali))
        
        total_ratio = 0
        for _, passi, totali in heap:
            total_ratio += passi / totali
        
        return total_ratio / len(classes)