"""
    Method 1 (By making enQueue operation costly) 
    This method makes sure that oldest entered element is always at the top of stack 1, 
    so that deQueue operation just pops from stack1. 
    To put the element at top of stack1, stack2 is used.

    Enqueue(x):
    While stack1 is not empty, push everything from stack1 to stack2.
    Push x to stack1 (assuming size of stacks is unlimited).
    Push everything back to stack1.
"""

class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self,x):
        while self.s1:
            k = self.s1.pop()
            self.s2.append(k)
        
        self.s1.append(x)

        while self.s2:
            v = self.s2.pop()
            self.s1.append(v)
    
    def dequeue(self):
        if len(self.s1) == 0:
            return "Q empty"
        
        x = self.s1.pop()
        return x
        
    def print(self):
        while self.s1:
            x = self.s1.pop()
            print(x)


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.dequeue())