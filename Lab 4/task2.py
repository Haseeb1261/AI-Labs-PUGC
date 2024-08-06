class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

queue = Queue()
print("Queue after initialization:", queue)
queue.enqueue(1)
print("Queue after enqueue:", queue)
queue.enqueue(2)
print("Queue after enqueues:", queue)
queue.enqueue(3)
print("Queue after enqueues:", queue)
print("Dequeued item:", queue.dequeue())
print("Queue after dequeue:", queue)
print("Peek item:", queue.peek())
print("Queue size:", queue.size())
