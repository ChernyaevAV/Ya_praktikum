# ID: 77913951

from typing import List


class MyDequeSized:
    def __init__(self, max_size: int):
        self.items: List[None, int] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.left: int = 0
        self.right: int = 0
        self.size: int = 0

    def push_back(self, value: int) -> None:
        """Добавляет элемент в конец дека.
        Если в деке уже находится максимальное число элементов,
        выводит «error»."""
        if self.size != self.max_size:
            if self.size == 0 and self.tail == self.head:
                self.head = (self.head - 1) % self.max_size
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.right = (self.tail - 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def push_front(self, value: int) -> None:
        """Добавляет элемент в начало дека.
        Если в деке уже находится максимальное число элементов,
        выводит «error»."""
        if self.size != self.max_size:
            if self.size == 0 and self.tail == self.head:
                self.tail = (self.tail + 1) % self.max_size
            self.items[self.head] = value
            self.head = (self.head - 1) % self.max_size
            self.left = (self.head + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop_back(self) -> int or str:
        """Выводит последний элемент дека и удалить его.
        Если дек был пуст, то выводит «error»."""
        if self.size == 0:
            return "error"
        value = self.items[self.right]
        self.items[self.right] = None
        self.tail = (self.tail - 1) % self.max_size
        self.right = (self.right - 1) % self.max_size
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = 0
            self.left = 0
            self.right = 0
        return value

    def pop_front(self) -> int or str:
        """Выводит первый элемент дека и удалить его.
        Если дек был пуст, то выводит «error»."""
        if self.size == 0:
            return "error"
        value = self.items[self.left]
        self.items[self.left] = None
        self.head = (self.head + 1) % self.max_size
        self.left = (self.left + 1) % self.max_size
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = 0
            self.left = 0
            self.right = 0
        return value


def read_input(num: int) -> List[(str or int)]:
    command_list = []
    for _ in range(num):
        command_list.append(input().strip().split(' '))

    return command_list


def main():
    n = int(input())
    max_size = int(input())
    command_list = read_input(n)
    queue = MyDequeSized(max_size)
    for command in command_list:
        if command[0] == 'push_back':
            queue.push_back(command[1])
        elif command[0] == 'push_front':
            queue.push_front(command[1])
        elif command[0] == 'pop_front':
            print(queue.pop_front())
        elif command[0] == 'pop_back':
            print(queue.pop_back())


if __name__ == '__main__':
    main()

