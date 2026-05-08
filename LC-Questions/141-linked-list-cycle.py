from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x): 
        self.val = x 
        self.next = None 

class Solution: 
    def hasCycleBruteForce(self, head: Optional[ListNode]) -> bool: 
        current = head 
        visited = set() 
        while current is not None: 
            if current in visited: 
                return True 
            visited.add(current) 
            current = current.next 
        return False 