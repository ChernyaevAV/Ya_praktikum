from typing import List


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value: int) -> None:
        if self.items:
            new_max = max(value, self.items[-1][1])
        else:
            new_max = value
        self.items.append((value, new_max))

    def pop(self) -> None:
        if len(self.items) != 0:
            self.items.pop()
        else:
            print('error')

    def get_max(self) -> int or None:
        if len(self.items):
            return self.items[-1][1]
        else:
            return None


def read_input(num: int) -> List[(str or int)]:
    command_list = []
    for _ in range(num):
        command_list.append(input().strip().split(' '))

    return command_list


def main():
    n = int(input())
    command_list = read_input(n)
    stack = Stack()
    for command in command_list:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'get_max':
            print(stack.get_max())


if __name__ == '__main__':
    main()
