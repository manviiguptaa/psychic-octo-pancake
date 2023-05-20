from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Add the new element to the empty queue1
        self.queue1.append(value)

        # Move back all elements from queue2 to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.queue1.popleft()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.queue1[0]

    def is_empty(self):
        return not self.queue1

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top())  # Output: 3

print("Popped element:", stack.pop())  # Output: 3

print("Top element after pop:", stack.top())  # Output: 2
