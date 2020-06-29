from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # add new item to tail if there is room in storage, set current pointer to tail
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        if len(self.storage) == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                # current pointer is at tail, add new item as head, set current pointer to head
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        buffer = []
        node = self.storage.head
        while node is not None:
            if node.value is not None:
                buffer.append(node.value)
            node = node.next
        return buffer