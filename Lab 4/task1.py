class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
    
stack = Stack()
print("Stack after initialization:", stack)
stack.push(1)
print("Stack after pushes:", stack)
stack.push(2)
print("Stack after pushes:", stack)
stack.push(3)
print("Stack after pushes:", stack)
print("Popped item:", stack.pop())
print("Stack after pop:", stack)
print("Peek item:", stack.peek())
print("Stack size:", stack.size())
