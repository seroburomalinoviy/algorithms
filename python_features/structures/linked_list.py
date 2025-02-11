from collections import namedtuple

Node = namedtuple("Node", "value next_node")


class LinkedListL:
    def __init__(self, value):
        self.tail_node = Node(value, None)
        self.new_node = None

    def pretend(self, value: int):
        self.new_node = Node(value, self.tail_node)
        self.tail_node = self.new_node

    def show(self):
        next_node = self.new_node
        while next_node:
            print(next_node.value)
            next_node = next_node.next_node


lst = LinkedListL(3)
lst.pretend(8)
lst.pretend(9)
lst.pretend(56)
lst.show()
print(type(lst))



class Nd:
    def __init__(self, value: int, next_node):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.value},{self.next_node})"


class LinkedListR:
    def __init__(self, value: int):
        self.tail = None
        self.prev_node = Nd(value, self.tail)
        self.head = self.prev_node
        self.current_node = None

    def append(self, value: int):
        self.current_node = Nd(value, self.tail)
        self.prev_node.next_node = self.current_node
        self.prev_node = self.current_node

    def show(self):
        next_node = self.head
        while next_node:
            print(next_node.value)
            next_node = next_node.next_node


rlst = LinkedListR(1)
rlst.append(4)
rlst.append(8)
rlst.append(9)
rlst.append(6)
rlst.show()

print(type(rlst))


class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.prev_node = prev_node
        self.next_node = next_node
        self.value = value

    def __repr__(self):
        return f"Node({self.value}, {self.next_node}, {self.prev_node})"



class LinkedListLR:
    def __init__(self, value):
        self.tail = Node()
        self.head = Node()
        self.prev_node = Node(value)
        self.head.next_node = self.prev_node
        self.tail.prev_node = self.prev_node

        self.current_node = None

    def pretend(self, value):
        self.current_node = Node(value, self.prev_node, None)
        self.head = self.current_node
        self.prev_node.prev_node = self.current_node
        self.prev_node = self.current_node

    def append(self, value):
        self.current_node = Node(value, None, self.prev_node)
        self.tail = self.current_node
        self.prev_node.next_node = self.current_node
        self.prev_node = self.current_node

    def show(self):
        next_node = self.head
        while next_node:
            print(next_node.value)
            next_node = next_node.next_node


ll = LinkedListLR(88)
ll.append(3)
ll.pretend(122)
ll.append(99)
ll.append(77)
ll.show()


