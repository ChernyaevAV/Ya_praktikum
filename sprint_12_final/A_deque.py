# ID: 78345811

from typing import List, Union


#  не получается вызвать исключение и продолжить исполнение кода
class DequeIsFullError(Exception):
    """Вызывается при попытке вставить в полный дэк"""


class EmptyDequeError(Exception):
    """Вызывается при запросе данных из пустого дэка"""


class MyDequeSized:
    def __init__(self, max_size: int):
        self.__queue: List[Union[None, int]] = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def _calc_idx(self, idx, add=False):
        """Двигает индекс впрово или влево"""
        idx = idx + 1 if add else idx - 1
        return idx % self.__max_size

    def _is_empty(self):
        """Проверяет пустой ли дек"""
        return self.__size == 0

    def push_front(self, item):
        """Добавляет значение в начало дека,
        если дек полный возвращает 'error'."""
        if self.__size >= self.__max_size:
            print('error')
        else:
            self.__head = self._calc_idx(self.__head)
            self.__queue[self.__head] = item
            self.__size += 1

    def push_back(self, item):
        """Добавляет значение в конец дека,
        если дек полный возвращает 'error'."""
        if self.__size >= self.__max_size:
            print('error')
        else:
            self.__queue[self.__tail] = item
            self.__tail = self._calc_idx(self.__tail, True)
            self.__size += 1

    def pop_front(self):
        """Удаляет и выводит значение из началао дека,
        если дек пустой возвращает 'error'."""
        if self._is_empty():
            return 'error'
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self._calc_idx(self.__head, True)
        self.__size -= 1
        return item

    def pop_back(self):
        """Удаляет и выводит значение из конца дека,
        если дек пустой возвращает 'error'."""
        if self._is_empty():
            return 'error'
        self.__tail = self._calc_idx(self.__tail)
        item = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__size -= 1
        return item


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
