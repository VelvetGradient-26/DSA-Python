class Deque: 
    def __init__(self):
        self.deque = []

    def is_empty(self): 
        if len(self.deque) == 0: 
            return True
        return False
    
    def insert_front(self, value): 
        self.deque.insert(0, value)

    def insert_back(self, value): 
        self.deque.append(value)

    def delete_front(self): 
        if self.is_empty(): 
            return "Deque is Empty"
        else: 
            return self.deque.pop(0)

    def delete_back(self): 
        if self.is_empty(): 
            return "Deque is Empty"
        else: 
            return self.deque.pop()
        
    def __len__(self): 
        return len(self.deque)
    
    def __str__(self): 
        result = ""
        for element in self.deque: 
            result += str(element) + " "
        return result
    
deque = Deque()

deque.insert_back(10)
deque.insert_front(20)
deque.insert_back(30)
deque.insert_back(40)
deque.insert_front(50)

print(deque)

print(deque.delete_back())
print(deque)
print(deque.delete_back())
print(deque)
print(deque.delete_front())
print(deque)
print(deque.delete_front())
print(deque)
print(deque.delete_back())
print(deque)
print(deque.delete_back())
print(deque)

