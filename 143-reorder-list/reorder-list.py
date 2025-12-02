# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head and not head.next:
            return 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None 
        curr = slow.next 
        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        slow.next = None
        first = head 
        second = prev 
        while second: 
            tmp1 = first.next 
            tmp2 = second.next 
            first.next = second 
            second.next = tmp1 
            first = tmp1 
            second = tmp2 



        