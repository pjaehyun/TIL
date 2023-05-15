# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#첫번째 풀이
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

# 두번째 풀이(코드 개선)
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        for _ in range(1, k):
            curr = curr.next
        begin = curr

        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        end = slow

        begin.val, end.val = end.val, begin.val
        return head