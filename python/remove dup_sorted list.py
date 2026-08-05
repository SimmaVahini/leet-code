# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to track the head of the modified list
        dummy = ListNode(0)
        dummy.next = head
        
        # 'pred' tracks the last known distinct node
        pred = dummy
        
        while head:
            # If it's the start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Move head to the end of the duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates by linking pred to the node after head
                pred.next = head.next
            else:
                # No duplicates, safe to advance pred
                pred = pred.next
                
            # Move forward in the list
            head = head.next
            
        return dummy.next
