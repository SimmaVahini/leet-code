# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
            
        # Dummy node handles edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node right before position 'left'
        for _ in range(left - 1):
            prev = prev.next
            
        # 'curr' is the first node of the sub-list to be reversed
        curr = prev.next
        
        # Link shifting loop
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
