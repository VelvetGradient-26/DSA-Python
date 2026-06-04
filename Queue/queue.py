class Queue: 
    def __init__(self): 
        self.queue = []

    def is_empty(self): 
        if len(self.queue) == 0: 
            return True
        return False
    
    def __len__(self): 
        return len(self.queue)
    
    def __str__(self): 
        result = ""
        for element in self.queue: 
            result += str(element) + " "
        return result
    
    def insert(self, value): 
        self.queue.append(value)

    def remove(self): 
        if self.is_empty(): 
            return "Queue is Empty"
        result = self.queue[0]
        del self.queue[0]
        return result
    
q = Queue()

for num in range(0, 101, 10): 
    q.insert(num)

print(q)

print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q)
    
