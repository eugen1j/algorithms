# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        second = head.next

        prev, slow = head, head.next
        size = 0

        while slow.next:
            size += 1
            prev.next = slow.next
            prev = slow
            slow = slow.next

        if size % 2 == 1:
            prev.next = None
            slow.next = second
        else:
            prev.next = second
            slow.next = None

        return head

