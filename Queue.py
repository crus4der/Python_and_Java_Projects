from _collections import deque

class Que:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return "the queue is empty"

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return print("the queue is empty")

    def empty(self):
        if not self.queue:
            print("Queue is empty :((")
        else:
            return print(self.queue)

    def clear(self):
        return self.queue.clear()

    def str(self):
        return str(self.queue)

    def len(self):
        return len(self.queue)

