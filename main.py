from stack import Stack
from queue import Queue

# Stack demo
s = Stack()
s.push(5)
s.push(15)
print("Stack pop:", s.pop())

# Queue demo
q = Queue()
q.enqueue(100)
q.enqueue(200)
print("Queue dequeue:", q.dequeue())
