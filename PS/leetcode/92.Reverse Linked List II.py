# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 첫번째 풀이
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        curr = head
        
        lst = deque()
        i = 1
        while curr:
            if left <= i <= right:
                lst.append(curr)
            curr = curr.next
            i += 1
        
        while len(lst) >= 2:
            curr_left = lst.popleft()
            curr_right = lst.pop()

            curr_left.val, curr_right.val = curr_right.val, curr_left.val
        return head
    
# 두번째 풀이
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        current, prev = head, None
        reverse_start, reverse_start_prev = None, None

        i = 1
        while current:
            _next = current.next
            
            if i == left:
                reverse_start = current
                reverse_start_prev = prev
            
            if left < i <= right:
                current.next = prev
            
            if right == i:
                reverse_start.next = _next
                if reverse_start_prev:
                    reverse_start_prev.next = current
                else:
                    head = current
            current, prev = _next, current
            i += 1
        return head
    
# 세번째 풀이
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next