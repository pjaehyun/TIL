# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_list(linked_list):
            res = []
            while linked_list:
                res.append(linked_list.val)
                linked_list = linked_list.next
            return res

        l1 = to_list(l1)
        l2 = to_list(l2)
        answer = None
        carry = 0
        while l1 or l2 or carry:
            _sum = carry

            if l1: _sum += l1.pop()
            if l2: _sum += l2.pop()
            
            node = ListNode(_sum % 10)
            node.next = answer
            answer = node

            carry = _sum // 10
        return answer