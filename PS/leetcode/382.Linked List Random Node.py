# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        random_num = randint(0, len(self.arr) - 1)
        return self.arr[random_num]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()