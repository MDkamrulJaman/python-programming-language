#!/usr/bin/env python3

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def __str__(self):
        # https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
        result = "\033[94m["
        for i in range(self.size):
            result += str(self.array[(self.head + i) % self.capacity]) + ", "
        result += "]\033[0m"
        return result

    def enqueue(self, elem):
        if self.size == self.capacity:
            print("Error: queue is full")
        else:
            self.array[self.tail] = elem
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Error: queue is empty")
            return None
        elem = self.array[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return elem


queue = ArrayQueue(10)
for i in range(0, 10):
    queue.enqueue(i)
print("queue:", queue)
print("dequeue:", queue.dequeue())
print("dequeue:", queue.dequeue())
print("queue:", queue)
