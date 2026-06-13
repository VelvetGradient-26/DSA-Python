class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value): 
        node = Node(value)
        if self.head is None: 
            self.head = node
            self.tail = node
            node.next = node            
        else: 
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.length += 1

    def prepend(self, value): 
        node = Node(value)
        if self.head is None: 
            self.head = node
            self.tail = node
            node.next = node
        else: 
            self.tail.next = node
            node.next = self.head
            self.head = node
        self.length += 1

    def insert(self, value, pos): 
        if pos < 0 or pos > self.length: 
            raise IndexError("Position out of Bounds")

        if pos == 0:  
            self.prepend(value)
            return
        
        if pos == self.length: 
            self.append(value)
            return 
        
        node = Node(value)
        current = self.head
        for _ in range(pos-1): 
            current = current.next
        node.next = current.next
        current.next = node
        self.length += 1

    def search(self, target): 
        current = self.head
        pos = 0
        if self.head is None: 
            return "Linked List is Empty"
        while True: 
            if current.value == target: 
                return f"Element found at Position: {pos}"
            current = current.next
            pos += 1
            
            if current == self.head: 
                break
        return "Element not found!"
    
    def get(self, pos): 
        if pos < 0 or pos > self.length - 1: 
            raise IndexError("Position out of Bounds")
        
        if pos == 0: 
            return self.head.value
        
        if pos == self.length - 1: 
            return self.tail.value
        
        current = self.head
        for _ in range(pos): 
            current = current.next

        return current.value
    
    def set(self, pos, value): 
        if pos < 0 or pos > self.length - 1: 
            raise IndexError("Position out of Bounds")

        if pos == 0: 
            self.head.value = value
            return self.head.value
        
        if pos == self.length - 1: 
            self.tail.value = value
            return self.tail.value
        
        current = self.head
        for _ in range(pos): 
            current = current.next
        current.value = value
        return current.value
        
    def __str__(self):
        if self.length == 0: 
            return "Circular Singly Linked List is Empty!"
        
        result = ""
        current = self.head
        while True: 
            result += str(current.value) + " -> "
            current = current.next

            if current == self.head: 
                break
        result += "Head"

        return result
    
    def __len__(self): 
        return self.length
    
cll = CircularSinglyLinkedList()

nums = [num for num in range(10, 101, 10)]
print(nums)

for num in nums: 
    cll.prepend(num)
print(cll)

for i in range(len(nums)): 
    print(cll.set(i, nums[i]))
