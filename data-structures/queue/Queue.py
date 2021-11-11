class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self , val):
        self.queue.append(val)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty."
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return "Queue is empty."
        
        return self.queue[0]
    
    def rear(self):
        if self.isEmpty():
            return "Queue is empty."
        
        return self.queue[len(self.queue) - 1]
    
    def print(self):
        if self.isEmpty():
            return "Queue is empty."
        
        for k in self.queue:
            print(k)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Front: {}".format(q.front()))
    print("Rear: {}".format(q.rear()))

    print(q.isEmpty())