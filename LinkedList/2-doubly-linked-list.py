class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
        self.length = 0

    def append(self, value): 
        node = Node(value)
        if self.head is None: 
            self.head = node
            self.length += 1
            return
        
        current = self.head
        while current.next is not None: 
            current = current.next
        current.next = node
        node.prev = current
        self.length += 1
    
    def prepend(self, value): 
        node = Node(value)
        if self.head is None: 
            self.head = node
            self.length += 1
            return
        
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, value, pos): 
        if self.head is None: 
            self.head = node
            self.length += 1
            return
        
        if pos == 1: 
            self.prepend(value)
            return
        
        if pos == self.length + 1: 
            self.append(value)
            return

        node = Node(value)
        current = self.head
        for _ in range(pos-2): 
            current = current.next
        
        node.prev = current
        node.next = current.next
        current.next.prev = node
        current.next = node
        
        self.length += 1

    def update(self, value, pos): 
        if self.head is None: 
            return "Linked List is Empty"
        if pos == 1: 
            self.head.value = value
            return
        
        current = self.head

        for _ in range(pos-1): 
            current = current.next
        current.value = value
        return
    
    def pop_front(self): 
        if self.head is None: 
            return "Linked List is Empty"
        
        self.head = self.head.next
        if self.head: 
            self.head.prev = None
        self.length -= 1
    
    def pop_back(self): 
        if self.head is None: 
            return "Linked List is Empty"
        
        if self.head.next is None: 
            self.head = None
            self.length -= 1
            return
        
        current = self.head
        while current.next is not None: 
            current = current.next
        
        current.prev.next = None
        current.prev = None
        self.length -= 1

    def delete(self, pos): 
        if self.head is None: 
            return "Linked List is Empty"
        
        if pos == 1: 
            self.pop_front()
            return
        
        if pos == self.length: 
            self.pop_back()
            return 
        
        current = self.head
        for _ in range(pos-2): 
            current = current.next

        del_node = current.next

        current.next.next.prev = current
        current.next = current.next.next

        del_node.next = None
        del_node.prev = None
        
        self.length -= 1

        
    def __str__(self): 
        result = ""
        current = self.head
        while current: 
            result += str(current.value) + " <-> "
            current = current.next
        result += "None"
        return result
    
    def __len__(self):
        return self.length


dl = DoublyLinkedList()

nums =[num for num in range(10, 101, 10)]

for num in nums: 
    dl.prepend(num)

dl.insert(45, 6) # insert at middle
dl.insert(110, 1) # insert at start
dl.insert(5, 13) # insert at end

dl.update(125, 1)
dl.update(46, 7)
dl.update(7, len(dl)-1)

dl.pop_front()
dl.pop_back()

dl.delete(6)

dl.insert(99, 2)

dl.update(101, 1)
print(dl)