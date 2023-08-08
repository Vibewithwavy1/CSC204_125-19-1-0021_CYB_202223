#To create a Queue data structure
class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def enqueue(self, data):
        self.queue.insert(data)
    
    def dequeue(self):
        if self.queue.head:
            data = self.queue.head.data
            self.queue.head = self.queue.head.next
            return data
        else:
            return None
    
    def display(self):
        self.queue.display()

#Test the queue data structure
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display() 
print(queue.dequeue())  
queue.display() 
