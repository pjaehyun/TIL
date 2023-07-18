class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.memory = {}
    
    def add(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def remove(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev

    def get(self, key: int) -> int:
        if key in self.memory:
            curr = self.memory[key]
            answer = curr.val
            del self.memory[key]
            self.remove(curr)
            self.add(curr)
            self.memory[key] = self.head.next
            return answer
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            curr = self.memory[key]
            del self.memory[key]
            self.remove(curr)
        
        if len(self.memory) == self.limit:
            del self.memory[self.tail.prev.key]
            self.remove(self.tail.prev)
        self.add(ListNode(key, value))
        self.memory[key] = self.head.next
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)