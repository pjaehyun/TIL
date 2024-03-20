# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 첫번째 풀이
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        right = list1
        left = right
        i = 0
        while right:
            if a <= i <= b:
                right = right.next
                i += 1
                continue
            if i > b:
                center = list2
                left.next = list2
                while center:
                    if center.next == None:
                        center.next = right
                        break
                    center = center.next
                break
            left = right
            right = right.next
            i += 1
        return list1
    
# 두번째 풀이
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        return list1