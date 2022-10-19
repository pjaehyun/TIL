# 직접 단어 수 카운트 후 정렬 첫번째 풀이
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        result = []
        for w in words:
            try:
                word_count[w] += 1
            except:
                word_count[w] = 1
        sorted_word = sorted([[k, v] for k, v in word_count.items()])
        sorted_word.sort(key=lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(sorted_word[i][0])
        return result


#Counter를 사용한 정렬 두번째 풀이
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = dict(Counter(words))
        word_count = sorted(word_count.items())
        word_count.sort(key=lambda x:x[1], reverse=True)
        return [a for (a, b) in word_count[:k]]


# 맥스힙을 사용한 세번째 풀이
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = dict(Counter(words))
        result = []
        max_heap = []
        heapq.heapify(max_heap)
        
        for k1, v in word_count.items():
            heapq.heappush(max_heap, (-v,k1))
            
        for i in range(k):
            item = heapq.heappop(max_heap)
            result.append(item[1])
        return result