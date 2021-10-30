# Approach use two stacks , one to store the min values

"""
    Push(x):
    - push x to first stack (one with the actual elements)
    - compare x with the top element of the auxilliary stack call this y
        - if x < y -> push x to the auxilliary stack
        - if x > y -> push y to the auxilliary stack
    
    Pop():
    - remove top element from the auxilliary stack and return the removed element
    - pop top from special stack (so auxilliary stack is updated for future operations)
    - pop top element from the main stack

    getMin():
    - return top element from the auxilliary stack
"""

class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100
    
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.max - 1
    
    def push(self, data):
        if self.isFull():
            print("Stack is full")
            return
        
        self.top += 1
        self.array.append(data)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        
        self.top -= 1
        return self.array.pop()


class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.Min = Stack()
    

    def push(self, x):
        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)
            y = self.Min.pop()
            self.Min.push(y)
            if x <= y:
                self.Min.push(x)
            else:
                self.Min.push(y)
    
    def pop(self):
        x = super().pop()
        self.Min.pop()
        return x
    
    def getMin(self):
        x = self.Min.pop()
        self.Min.push(x)
        return x

# driver method for testing

if __name__ == "__main__":
    ss = SpecialStack()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(-1)

    print(ss.getMin())