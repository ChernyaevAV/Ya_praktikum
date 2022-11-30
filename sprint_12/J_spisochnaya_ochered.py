from typing import List


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def get(self):
        if self.head is None:
            return 'error'
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return temp.value

    def put(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count


def read_input(num: int) -> List[(str or int)]:
    command_list = []
    for _ in range(num):
        command_list.append(input().strip().split(' '))

    return command_list


def main():
    n = int(input())
    command_list = read_input(n)
    queue = Queue()
    for command in command_list:
        if command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'get':
            print(queue.get())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()
