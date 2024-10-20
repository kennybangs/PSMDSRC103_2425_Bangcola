# -*- coding: utf-8 -*-

"""
For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer science data structure. A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain a specific order. When you want to get something off the end of a queue, you get the item that has been in there the longest (this is known as ‘first-in-first-out’, or FIFO). You can read up on queues at Wikipedia if you’d like to learn more.

Create a new file called queue.py to make your Queue class. In your Queue class, you will need three methods:

init : to initialize your Queue (think: how will you store the queue’s elements? You’ll need to initialize an appropriate object attribute in this method)
insert: inserts one element in your Queue
remove: removes one element from your Queue and returns it. If the queue is empty, return a message that says it is empty (without throwing an error that halts your code).
When you’re done, you should test your implementation. Your results should look like this:


"""

class Queue():
    
    def __init__(self):
        self.queue = []
        
    def insert(self,item):
        self.queue.append(item)
    
    def remove(self):
       if len(self.queue) == 0:
           print('the queue is empty')
       else:
           print(self.queue.pop(0))
           
queue = Queue()        
queue.insert(5)
queue.insert(6)
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
queue.remove()