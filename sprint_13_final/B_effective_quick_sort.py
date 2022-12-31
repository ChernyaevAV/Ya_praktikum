# ID: 80195365
from typing import List


# class Candidate:
#     def __init__(self, name, completed, penalty):
#         self.__name = name
#         self.__completed = -int(completed)
#         self.__penalty = int(penalty)
#
#     def __convert(self):
#         return [self.__completed, self.__penalty, self.__name]
#
#     def __lt__(self, other):
#         return self.__convert() < other.__convert()
#
#     def __str__(self):
#         return self.__name


def quicksort(array: List[object], start: int, end: int) -> None:
    if end - start > 1:
        p = partition(array, start, end)
        quicksort(array, start, p)
        quicksort(array, p + 1, end)


def partition(array: List[object], left: int, right: int) -> int:
    pivot = array[left]
    l = left + 1
    r = right - 1

    while True:
        while l <= r and array[l] < pivot:
            l += 1
        while l <= r and array[r] > pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
        else:
            array[left], array[r] = array[r], array[left]
            return r


def main():
    n = int(input())
    # candidates = [Candidate(*input().strip().split()) for _ in range(n)]
    # quicksort(candidates, 0, len(candidates))
    # print(*candidates, sep='\n')

    candidates = [[-int(completed), int(penalty), name]
                  for name, completed, penalty
                  in [input().strip().split() for _ in range(n)]]
    quicksort(candidates, 0, len(candidates))

    for item in candidates:
        print(item[-1])


if __name__ == '__main__':
    main()
