# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize

class Stack:
    def __init__(self):
        self.stack = []
    

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self , element):
        self.stack.append(element)
    
    def _pop(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        return self.stack[len(self.stack) - 1]

    def print(self):
        while not self.isEmpty():
            val = self.stack.pop()
            print(val)

# Implemeting Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:
    #initialize root of the linked list
    def __init__(self):
        self.root = None
    
    # Ternary Operator
    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self, val):
        node = Node(val)

        node.next = self.root

        self.root = node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        curr = self.root

        self.root = self.root.next

        return curr.data
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.root.data
    
    def print(self):
        curr = self.root

        if curr is None:
            return "Stack is Empty"
        
        while curr:
            print(curr.data)
            curr = curr.next

s = StackLL()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(10)
s.pop()
s.print()
print("00-00")
print(s.peek())

