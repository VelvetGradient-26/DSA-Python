class Node: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 

class MyLinkedList: 
    def __init__(self): 
        self.head = None  
        self.tail = None 
        self.length = 0 
    
    def get(self, index: int) -> int: 
        if index >= self.length or index < 0: 
            return -1 
        current = self.head 
        for _ in range(index): 
            current = current.next             
        result = current.val            
        return result       

    def addAtHead(self, val: int) -> None: 
        node = Node(val) 
        if self.head is None: 
            self.head = node 
            self.tail = node 
        else: 
            node.next = self.head 
            self.head = node 
        self.length += 1 

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None: 
            self.head = node
            self.tail = node
        else: 
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length: 
            self.addAtTail(val)
        elif index == 0: 
            self.addAtHead(val)
        elif index > self.length: 
            return -1
        else:
            node = Node(val)
            current = self.head
            for _ in range(index - 1): 
                current = current.next
            node.next = current.next
            current.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0: 
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self.length -= 1

    def __str__(self): 
        if self.length == 0: 
            return "Linked List is Empty"
        result = ""
        current = self.head
        while current is not None: 
            result += str(current.val) + " -> "
            current = current.next
        result += "None"
        return result

    def __len__(self): 
        return self.length

## TESTS
ll = MyLinkedList()

ll.addAtHead(1)   
print(ll)   
ll.addAtTail(3)
print(ll) 
ll.addAtIndex(1, 2)
print(ll) 
ll.get(1)
print(ll) 
ll.deleteAtIndex(1)
print(ll) 
ll.get(1)
print(ll) 