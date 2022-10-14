# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        count_node = head
        while count_node:
            cnt += 1
            count_node = count_node.next
        n = cnt // 2
        
        if n == 0: return None

        i, temp = 1, head
        while i < n:
            temp = temp.next
            i += 1
        if temp.next.next == None:
            temp.next = None
        else:
            temp.next = temp.next.next
        return head