# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        slow = fast = head
        while(fast and fast.next):
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = temp.next.next
        return head
