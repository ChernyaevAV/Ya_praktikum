from typing import List


class MyQueueSized:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_queue = 0

    def push(self, value: int) -> None:
        if self.size_queue != self.max_size:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size_queue += 1
        else:
            print("error")

    def pop(self) -> int or None:
        if self.size_queue <= 0:
            return None
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_queue -= 1
        return value

    def peek(self) -> int or None:
        if self.size_queue == 0:
            return None
        return self.items[self.head]

    def size(self) -> int:
        return self.size_queue


def read_input(num: int) -> List[(str or int)]:
    command_list = []
    for _ in range(num):
        command_list.append(input().strip().split(' '))

    return command_list


def main():
    n = int(input())
    max_size = int(input())
    command_list = read_input(n)
    queue = MyQueueSized(max_size)
    for command in command_list:
        if command[0] == 'push':
            queue.push(command[1])
        elif command[0] == 'pop':
            print(queue.pop())
        elif command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()
