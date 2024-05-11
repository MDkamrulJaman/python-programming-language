#!/usr/bin/env python3

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = "[ "
        current = self.head
        while current:
            if current != self.head:
                string += " -> "
            string += str(current.data)
            current = current.next
        string += " ]"
        return string

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    def delete(self, data):
        previous = None
        current = self.head
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                # unlink the node from the list
                current.next = None
                return
            else:
                previous = current
                current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        # implementation goes here
        pass

    def new_reversed_list(self):
        # implementation goes here
        pass

    def append_list(self, llist):
        # implementation goes here
        pass


ll = LinkedList()
ll.insert('a')
ll.insert('l')
ll.insert('g')
ll.insert('o')
ll.insert(2)
ll.insert(0)
ll.insert(2)
ll.delete(4)
#print(ll.head.data)
#print(ll.head.next.data)
#print(ll.head.next.next.data)
#print(ll.search(7))

ll = LinkedList()
ll.insert('l')
ll.insert('e')
ll.insert('g')
ll.insert('o')
print(ll)
ll.delete('e')
ll.prepend('a')
print(ll)
elem = ll.search('o')
print(elem)
print("list size: ", ll.size())
