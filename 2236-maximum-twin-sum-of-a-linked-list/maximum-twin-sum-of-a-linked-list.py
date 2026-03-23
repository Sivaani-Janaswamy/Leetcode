# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        #reversing
        curr = slow
        prev = None
        while(curr):
            newnode = curr.next
            curr.next = prev
            prev = curr
            curr = newnode
        twinsum = 0
        while(prev and head):
            twinsum = max(twinsum,prev.val+head.val)
            head = head.next
            prev = prev.next
        return twinsum
            

        
            

        