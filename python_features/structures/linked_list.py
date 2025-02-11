from collections import namedtuple

Node = namedtuple("Node", "value next_node")


class LinkedListL:
    def __init__(self, value):
        self.tail_node = Node(value, None)
        self.new_node = None

    def prepend(self, value: int):
        self.new_node = Node(value, self.tail_node)
        self.tail_node = self.new_node

    def show(self):
        next_node = self.new_node
        while next_node:
            print(next_node.value)
            next_node = next_node.next_node


lst = LinkedListL(3)
lst.prepend(8)
lst.prepend(9)
lst.prepend(56)
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
    """
    Двусвязный список
    Главное свойство - добавление элементов в начало и в конец списка

    Описание структуры
    - список состоит из нод. Нода содержит ссылку на предыдущую ноду, на следующую, и значение
    - первый элемент списка, голова, содержит в себе ссылку на первую ноду
    - последний элементы, хвост, на последнюю ноду

    Операция добавления элемента в конец списка
    создаем новую ноду со значением и Нан в ссылке на следующую ноду
    меняем ссылку хвоста на текущую ноду
    меняем в текущей ноде сслыку на следующую ноду - ссылаемся на новую ноду
    помечаем новую ноду как текущую
    """
    def __init__(self, value):
        self.prev_node = Node(value)
        self.head = self.prev_node
        self.tail = self.prev_node

    def prepend(self, value):
        next_node = self.head
        current_node = Node(value, next_node, None)
        next_node.prev_node = current_node
        self.head = current_node

    def append(self, value):
        prev_node = self.tail
        current_node = Node(value, None, prev_node)
        prev_node.next_node = current_node
        self.tail = current_node

    def show(self):
        next_node = self.head
        while next_node:
            print(next_node.value)
            next_node = next_node.next_node


ll = LinkedListLR(88)
ll.append(3)
ll.append(99)
ll.prepend(9898)
ll.append(11)
ll.append(22)
ll.prepend(1234)
ll.append(33)
ll.append(44)
ll.append(55)
ll.prepend(10000000)
ll.show()
print(type(ll))


class MultiToolForLinkedList(LinkedListLR):
    def __init__(self, value):
        super().__init__(value)

    def delete(self, value) -> None:
        node = self.head
        while node:
            if node.value == value:
                if node == self.head:
                    next_node = node.next_node
                    self.head = next_node
                elif node == self.tail:
                    prev_node = node.prev_node
                    self.tail = prev_node
                else:
                    prev_node = node.prev_node
                    next_node = node.next_node
                    prev_node.next_node = node.next_node
                    next_node.prev_node = node.prev_node
                return
            node = node.next_node

    def insert(self, index, value):
        pass


llst = MultiToolForLinkedList(8)
llst.append(1)
llst.prepend(99)
llst.prepend(900)
llst.show()
llst.delete(8)
llst.delete(99)
llst.delete(900)
print("---")
llst.show()
print(type(llst))


class UpgradedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.tail is None or self.head is None:
            current_node = Node(value)
            self.head = current_node
            self.tail = current_node
        else:
            last_node = self.tail
            current_node = Node(value, None, last_node)
            last_node.next_node = current_node
            self.tail = current_node

    def prepend(self, value):
        if self.tail is None or self.head is None:
            current_node = Node(value)
            self.head = current_node
            self.tail = current_node
        else:
            first_node = self.head
            current_node = Node(value, first_node, None)
            first_node.prev_node = current_node
            self.head = current_node

    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node == self.head:
                    self.head = node.next_node
                elif node == self.tail:
                    self.tail = node.prev_node
                else:
                    next_node = node.next_node
                    prev_node = node.prev_node
                    next_node.prev_node = prev_node
                    prev_node.next_node = next_node
                return
            node = node.next_node

    def insert(self, index, value):
        counter = 0
        node = self.head
        while node:
            if index == counter:
                if node == self.head:
                    self.prepend(value)
                elif node == self.tail:
                    last_node = self.tail
                    prev_node = last_node.prev_node
                    current_node = Node(value, last_node, prev_node)
                    prev_node.next_node = current_node
                    last_node.prev_node = current_node
                else:
                    next_node = node.next_node
                    new_node = Node(value, node.next_node, node)
                    node.next_node = new_node
                    next_node.prev_node = new_node
                return
            counter += 1
            node = node.next_node

    def reverse(self):
        pass

    def clear(self):
        self.head = None
        self.tail = None

    def show(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next_node


updll = UpgradedLinkedList()
updll.append(1)
updll.append(3)
updll.insert(1, 2)
updll.show()



