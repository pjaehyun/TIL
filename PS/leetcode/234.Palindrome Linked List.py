# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next
        
        l, r = 0, len(lst) - 1
        while l < r and lst[l] == lst[r]:
            l += 1
            r -= 1
        return l >= r