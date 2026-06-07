from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next is not None: 
            if current.next.val == current.val: 
                # victim = current.next
                current.next = current.next.next
                # victim.next = None
            else: 
                current = current.next
        
        return head
        