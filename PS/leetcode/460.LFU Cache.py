# 다른 해답 참고해서 풀이
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.count = defaultdict(OrderedDict)
        self.lf = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.update(node, node.value)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                k, v = self.count[self.lf].popitem(last=False)
                self.cache.pop(k)    
            node = ListNode(key, value)
            self.cache[key] = node
            self.count[1][key] = value
            self.lf = 1
        else:
            node = self.cache[key]
            node.value = value
            self.update(node, value)
            

    def update(self, node, value):
        key, freq = node.key, node.freq
        self.count[freq].pop(key)
        
        if not self.count[freq] and self.lf == freq:
            self.lf += 1
        self.count[freq+1][key] = value
        node.freq += 1
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)