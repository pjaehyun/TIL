# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        begin = None

        i = 1
        temp = head
        while temp:
            if i == k:
                begin = temp
            temp = temp.next
            i += 1

        n = i-1
        i = 1
        temp = head
        while temp:
            if i + k - 1 == n:
                end_val = temp.val
                temp.val = begin.val
                begin.val = end_val
                return head
            temp = temp.next
            i += 1