class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def front_element(self):
        if self.is_empty():
            return None
        return self.front.get_data()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.set_next(new_node)
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.get_data()
        self.front = self.front.get_next()
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return data

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer

if __name__ == "__main__":
    queue = LinkedQueue()

    queue.enqueue(Order(5, "Alice"))
    queue.enqueue(Order(3, "Bob"))
    queue.enqueue(Order(10, "Charlie"))

    node = queue.front 
    while node is not None:
        order = node.get_data()
        order.print()
        node = node.get_next()