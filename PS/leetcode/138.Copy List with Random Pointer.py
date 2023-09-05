"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {}
        temp = head
        while temp:
            table[temp] = Node(temp.val, temp.next, None)
            temp = temp.next
        
        res = Node(0)
        temp = res
        while head:
            temp.next = table[head]
            if head.random:
                temp.next.random = table[head.random]
            head = head.next
            temp = temp.next
        return res.next