class StackEmpty(Exception):
    pass

class Stack: 
    def __init__(self): 
        self.stack = []

    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        result = ""
        for i in range(len(self.stack) - 1, -1, -1):
            result += str(self.stack[i]) + " "
        return result

    def is_empty(self): 
        if len(self.stack) == 0: 
            return True 
        return False
 
    def push(self, value): 
        self.stack.append(value)

    def pop(self): 
        element = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return element
    
    def peek(self):
        if len(self.stack) == 0: 
            raise StackEmpty("Stack is Empty")
        else:  
            return self.stack[len(self.stack) -1]
        
stack = Stack()
print(stack.peek())
for num in range(0, 101, 10): 
    stack.push(num)


print(stack)
print(stack.is_empty())
for num in range(len(stack) + 1):
    print(stack.pop())