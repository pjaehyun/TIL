# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            res = 0
            idx = 1
            while idx <= b:
                if a % idx == 0 and b % idx == 0:
                    res = idx
                idx += 1
            return res
        
        node1 = head
        while node1.next:
            node2 = node1.next
            gcd_value = gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2

        return head