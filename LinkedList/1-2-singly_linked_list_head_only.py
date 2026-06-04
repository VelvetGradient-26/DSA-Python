import random 

class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
        self.length = 0

    def prepend(self, value): 
        node = Node(value)

        if self.head is None: 
            self.head = node
            self.length += 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1
        
    def append(self, value): 
        node = Node(value)
        
        if self.head is None: 
            self.head = node
            self.length += 1 
        else:
            current = self.head
            while current.next is not None: 
                current = current.next
            current.next = node
            self.length += 1
    
    def insert(self, value, pos): 
        node = Node(value)

        if pos == 0: 
            self.prepend(value)
        elif pos == (self.length - 1): 
            self.append(value)
        else: 
            current = self.head
            for _ in range(pos - 1): 
                current = current.next
            node.next = current.next
            current.next = node
            self.length += 1

    def update(self, value, pos): 
        if pos == 0: 
            self.head.value = value
        else:
            current = self.head
            for _ in range(pos): 
               current = current.next 
            current.value = value

    def delete(self, pos): 
        if pos == 0: 
            self.head = self.head.next
            self.length -= 1
        current = self.head
        for _ in range(pos - 1): 
            current = current.next
        current.next = current.next.next 
        self.length -= 1

    def __str__(self): 
        current = self.head
        result = ""
        while current is not None: 
            result += (str(current.value) + " -> ")
            current = current.next
        result += "None" 
        return result

    def __len__(self): 
        return self.length


linkedlist = LinkedList()

random.seed(42)
nums = [random.randint(1,100) for _ in range(10)]
print(nums)
for num in nums: 
    print(num, end = " ")
    linkedlist.prepend(num)

linkedlist.insert(42, 9)
print("\n",linkedlist)
linkedlist.update(69, 0)
print("\n",linkedlist)
linkedlist.update(100, 8)
print("\n", linkedlist)
linkedlist.delete(10)
# linkedlist.delete(2)
print("\n", linkedlist)


