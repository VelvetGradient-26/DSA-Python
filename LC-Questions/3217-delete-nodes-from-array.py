from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        check = set(nums)
        current = head
        while head and head.val in check: 
            head = head.next

        while current and current.next: 
            if current.next.val in check:
                current.next = current.next.next
            else: 
                current = current.next

        return head 


        