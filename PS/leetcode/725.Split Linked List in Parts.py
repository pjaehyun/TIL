# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 첫번째 풀이
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = []

        head_len = 0
        temp = head
        while temp:
            temp = temp.next
            head_len += 1
        
        n = head_len // k
        mod = head_len % k
        
        sep = [n for _ in range(k)]
        i = 0
        while mod > 0:
            sep[i % k] += 1
            mod -= 1
            i += 1

        answer = []
        for i in range(k):
            res = ListNode()
            temp = res
            while sep[i] > 0:
                temp.next = ListNode(head.val)
                head = head.next
                temp = temp.next
                sep[i] -= 1
            answer.append(res.next)
        return answer
    
# 두번째 풀이
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        size, curr, answer = 0, head, []

        while curr:
            curr = curr.next
            size += 1
        
        n = size // k
        mod = size % k

        curr = head
        prev = None
        for i in range(k):
            dummy = curr

            for _ in range(n + (mod > 0)):
                prev = curr
                curr = curr.next
            if mod > 0:
                mod -= 1
            if prev:
                prev.next = None
            answer.append(dummy)
        return answer
